Plan
1. Define Core Goals

Input: Student interests (keywords, chosen domain, or skill level).

Output:

3–5 project suggestions with short descriptions.

Web resource links (GitHub repos, tutorials, official docs, blogs).

Mode of Delivery: As conversational suggestions inside Copilot Chat/Agent Mode.

2. Tech Stack

Copilot Agent Mode: Orchestrates reasoning + retrieval of resources.

Knowledge Sources:

GitHub repositories (search API).

Educational sites (Coursera, freeCodeCamp, W3Schools, Medium, etc.).

Open courseware (MIT OCW, Stanford Online).

Middleware: LangChain or Semantic Kernel (optional, if you need orchestration logic beyond Copilot).

Frontend:



Option B: Web app (React + Copilot SDK).

3. Architecture

Student Query Layer

User specifies interest (e.g., “AI + beginner”).

Copilot Agent Mode

Calls retrieval plugins:

GitHub Search API → fetch projects.

Custom Knowledge Index (vector DB with curated resource links).

Ranks by relevance (difficulty level, recency, stars, trustworthiness).

Response Generator

Formats suggestions into:

Project Title

Why this project matters (skill/learning outcome).

Resource links (GitHub, docs, tutorials).

4. Features to Implement

Interest-Based Filtering

Beginner, Intermediate, Advanced.

Domains (AI, Web, Security, Systems, Cloud, Data Science).

Explainability

Each suggestion carries a reason: “This project helps you practice dynamic programming + recursion.”

Progressive Path

Recommend “starter → advanced → capstone” projects.

One-Click Open

Direct “Open in VS Code” or “Fork repo” buttons.

5. Development Roadmap
Phase 1 – Foundation (2 weeks)

Setup Copilot Agent Mode playground.

Integrate GitHub Search API.

Define interest taxonomy (list of categories).

Phase 2 – Smart Retrieval (3–4 weeks)

Build project ranking logic (by stars, forks, activity).

Create a lightweight vector DB with curated resource links.

Add Copilot prompt templates (e.g., “Suggest 3 AI beginner projects with links.”).

Phase 3 – Experience Layer (2 weeks)

Build VS Code integration or web app UI.

Format results into structured cards (Project + Links + Learning outcomes).

Phase 4 – Enrichment (Continuous)

Add personalized learning paths.

Track student’s completed projects.

Integrate with MS Teams/Outlook for study reminders.

🌱 Example Output

Student Input: “I’m interested in Web Development, beginner level.”

Copilot Suggestion:

Build a Personal Portfolio Website

Skills: HTML, CSS, GitHub Pages.

Repo: GitHub Starter Portfolio

Resource: freeCodeCamp HTML/CSS Guide

Todo App with React

Skills: React basics, state management.

Repo: TodoMVC in React

Resource: React Docs

Weather Dashboard using APIs

Skills: REST APIs, JavaScript fetch.

Repo: Weather App Example

Resource: MDN Web Docs Fetch API