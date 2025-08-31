import argparse
from .agent import ProjectMentorAgent

def main():
    """Main function to run the CLI."""
    parser = argparse.ArgumentParser(description="Get project suggestions from the ProjectMentorAgent.")
    parser.add_argument("--interest", type=str, required=True, help="Your area of interest (e.g., 'web development', 'machine learning').")
    parser.add_argument("--skill-level", type=str, required=True, choices=['beginner', 'intermediate', 'advanced'], help="Your skill level.")

    args = parser.parse_args()

    agent = ProjectMentorAgent()
    suggestions = agent.get_project_suggestions(args.interest, args.skill_level)

    print("\n--- Project Suggestions ---")
    print(suggestions)

if __name__ == "__main__":
    main()

