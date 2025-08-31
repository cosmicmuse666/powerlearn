import requests
from datetime import datetime, timezone
import math

def search_github_projects(query: str, language: str = None, max_results: int = 50):
    """
    Search for project repositories on GitHub based on keywords and language.
    Fetches more results to provide a better pool for ranking.
    """
    base_url = "https://api.github.com/search/repositories"
    query_parts = [query]
    if language:
        query_parts.append(f"language:{language}")
    
    q = " ".join(query_parts)

    params = {
        "q": q,
        "sort": "stars",
        "order": "desc",
        "per_page": max_results
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()["items"]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while searching GitHub: {e}")
        return []

def rank_github_projects(projects: list, interest: str, skill_level: str):
    """
    Ranks projects based on an advanced scoring system with normalized scores,
    tailored to the user's skill level.
    """
    if not projects:
        return []

    # --- Skill Level Weights ---
    if skill_level == 'beginner':
        weights = {'stars': 0.2, 'forks': 0.1, 'recency': 0.25, 'maintenance': 0.25, 'relevance': 0.2}
    elif skill_level == 'advanced':
        weights = {'stars': 0.4, 'forks': 0.25, 'recency': 0.1, 'maintenance': 0.1, 'relevance': 0.15}
    else: # Intermediate
        weights = {'stars': 0.3, 'forks': 0.15, 'recency': 0.15, 'maintenance': 0.2, 'relevance': 0.2}

    # --- Normalization --- 
    max_stars = max(p['stargazers_count'] for p in projects) or 1
    max_forks = max(p['forks_count'] for p in projects) or 1

    for project in projects:
        # --- Scoring Components ---
        stars_score = project['stargazers_count'] / max_stars
        forks_score = project['forks_count'] / max_forks

        pushed_at = datetime.strptime(project['pushed_at'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
        age_in_days = (datetime.now(timezone.utc) - pushed_at).days
        recency_score = max(0, 1 - (age_in_days / 365))

        issue_penalty = 1 - min(1, project['open_issues_count'] / 100)
        license_bonus = 0.1 if project.get('license') else 0
        maintenance_score = issue_penalty + license_bonus

        interest_topics = set(interest.lower().split())
        project_topics = set(t.lower() for t in project.get('topics', []))
        relevance_score = len(interest_topics.intersection(project_topics)) / len(interest_topics) if interest_topics else 0

        # --- Final Score Calculation ---
        project['score'] = (
            stars_score * weights['stars'] + 
            forks_score * weights['forks'] + 
            recency_score * weights['recency'] + 
            maintenance_score * weights['maintenance'] + 
            relevance_score * weights['relevance']
        )

    return sorted(projects, key=lambda p: p['score'], reverse=True)
