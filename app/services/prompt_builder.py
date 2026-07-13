from app.core.custom_exceptions import PromptGenerationError


def build_project_prompt(analysis: dict) -> str:
    try:
        languages = ", ".join(analysis["languages"])

        config_files = (
            ", ".join(analysis["configuration_files"])
            if analysis["configuration_files"]
            else "None"
        )

        prompt = f"""
You are an expert software engineer.

Analyze the following software project.

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

Your tasks:

1. Explain what this project does.
2. Explain the architecture.
3. Explain the execution flow.
4. Explain each technology being used.
5. Suggest improvements.
6. Estimate the difficulty level.
7. Recommend a learning order for the source code.

Return the explanation in clear English suitable for a beginner.
"""

        return prompt.strip()

    except KeyError as e:
        raise PromptGenerationError(f"Missing required analysis field: {e}")

    except Exception as e:
        raise PromptGenerationError(f"Failed to generate project prompt: {e}")