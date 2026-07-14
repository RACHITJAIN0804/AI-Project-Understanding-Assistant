from pathlib import Path


HIGH_PRIORITY_FILES = {
    "README.md",
    "main.py",
    "app.py",
    "manage.py",
    "index.js",
    "server.js",
}

MEDIUM_PRIORITY_FILES = {
    "requirements.txt",
    "package.json",
    "pom.xml",
    "build.gradle",
    "Dockerfile",
    "docker-compose.yml",
    ".env.example",
}

HIGH_PRIORITY_FOLDERS = {
    "controllers",
    "controller",
    "routes",
    "router",
    "services",
    "service",
}

MEDIUM_PRIORITY_FOLDERS = {
    "models",
    "model",
    "entities",
    "entity",
    "schemas",
    "schema",
}


MAX_FILE_SIZE = 5000
MAX_TOTAL_CONTEXT = 30000


def build_project_context(project_files: list[dict]) -> str:
    high_priority = []
    medium_priority = []
    normal_priority = []

    for file in project_files:
        file_name = Path(file["name"]).name
        folder_names = {part.lower() for part in Path(file["path"]).parts}

        if (
            file_name in HIGH_PRIORITY_FILES
            or folder_names.intersection(HIGH_PRIORITY_FOLDERS)
        ):
            high_priority.append(file)

        elif (
            file_name in MEDIUM_PRIORITY_FILES
            or folder_names.intersection(MEDIUM_PRIORITY_FOLDERS)
        ):
            medium_priority.append(file)

        else:
            normal_priority.append(file)

    selected_files = high_priority + medium_priority + normal_priority

    context_parts = []
    total_size = 0

    for file in selected_files:
        content = file["content"][:MAX_FILE_SIZE]

        section = (
            f"File: {file['path']}\n"
            f"{'-' * 60}\n"
            f"{content}\n\n"
        )

        if total_size + len(section) > MAX_TOTAL_CONTEXT:
            break

        context_parts.append(section)
        total_size += len(section)

    return "".join(context_parts)