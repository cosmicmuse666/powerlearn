import os
import json
from .api_clients import search_github_projects, rank_github_projects

class ProjectMentorAgent:
    def __init__(self):
        self.resources = self._load_resources()

    def _load_resources(self):
        """Loads the curated resources from the JSON file."""
        try:
            with open("src/resources.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def get_project_suggestions(self, interest: str, skill_level: str, language: str = None):
        """
        Generates project suggestions based on student's interest and skill level.
        """
        print(f"Generating project suggestions for interest: '{interest}', skill level: '{skill_level}', language: '{language}'...")

        # Search for relevant projects on GitHub
        github_projects = search_github_projects(query=interest, language=language, max_results=50)
        
        # Rank the fetched projects
        ranked_projects = rank_github_projects(github_projects, interest, skill_level)

        # Get project ideas from the simulated LLM, using the top 10 ranked projects
        llm_suggestions = self._get_simulated_llm_response(interest, skill_level, ranked_projects[:10])

        return llm_suggestions

    def _get_simulated_llm_response(self, interest: str, skill_level: str, github_projects: list):
        """A private method to simulate the LLM's response, now with dynamic data and a learning path."""
        
        project_suggestions = []
        for i, project in enumerate(github_projects):
            suggestion = (
                f"{i+1}. {project['name']}\n"
                f"   - Why: {project['description']}\n"
                f"   - Repo: {project['html_url']}\n"
                f"   - Level: {skill_level.capitalize()}"
            )
            project_suggestions.append(suggestion)

        # Add a progressive learning path
        learning_path = [f"\n✨ Learning Path Tip:"]
        if len(github_projects) > 1:
            learning_path.append(f"For a progressive learning experience, we suggest the following order:")
            for i, project in enumerate(github_projects):
                learning_path.append(f"{i+1}. Start with '{project['name']}'.")
            if len(github_projects) > 2:
                learning_path.append("This path will build your skills from foundational to more complex concepts.")
        
        project_suggestions.extend(learning_path)

        # Add curated resources
        if interest.lower() in self.resources:
            resource = self.resources[interest.lower()][0]
            project_suggestions.append(f"\nResource Recommendation:\n- {resource['title']}: {resource['url']}")

        return "\n".join(project_suggestions)
