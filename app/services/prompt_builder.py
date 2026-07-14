def build_project_prompt(analysis: dict, project_context: str) -> str:
    languages = ", ".join(analysis["languages"])

    config_files = (
        ", ".join(analysis["configuration_files"])
        if analysis["configuration_files"]
        else "None"
    )

    prompt = f"""
You are an expert software engineer and software architecture mentor.

Analyze the following software project.

Project Information

Project Name:
{analysis["project_name"]}

Framework:
{analysis["framework"]}

Architecture:
{analysis["architecture"]}

Programming Languages:
{languages}

Project Size:
{analysis["project_size"]}

Entry Point:
{analysis["entry_point"]}

Database:
{analysis["database"]}

README Present:
{analysis["readme_present"]}

Configuration Files:
{config_files}

Repository Source Code

{project_context}

Your tasks:

1. Explain the purpose of the project.
2. Explain the architecture.
3. Explain the execution flow from start to finish.
4. Explain the role of every major file.
5. Explain the technologies and frameworks used.
6. Suggest possible improvements.
7. Estimate the project difficulty.
8. Recommend a learning order for understanding the project.

Respond in beginner-friendly English with proper headings.
"""

    return prompt.strip()