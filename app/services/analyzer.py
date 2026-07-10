from pathlib import Path


LANGUAGE_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".html": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".md": "Markdown",
    ".xml": "XML",
    ".yml": "YAML",
    ".yaml": "YAML",
    ".sql": "SQL",
}


ENTRY_FILES = [
    "main.py",
    "app.py",
    "index.html",
    "index.js",
    "server.js",
]


CONFIG_FILES = [
    "requirements.txt",
    "package.json",
    "pom.xml",
    "Dockerfile",
    ".env.example",
]


def analyze_repository(repository_path: Path, project_files: list) -> dict:
    """
    Analyze repository metadata.
    """

    languages = set()

    file_paths = []

    readme_present = False

    entry_point = None

    configuration_files = []

    for project_file in project_files:

        extension = project_file["extension"]

        if extension in LANGUAGE_MAP:
            languages.add(LANGUAGE_MAP[extension])

        file_name = project_file["name"]

        file_paths.append(project_file["path"])

        if file_name.lower().startswith("readme"):
            readme_present = True

        if file_name in ENTRY_FILES and entry_point is None:
            entry_point = project_file["path"]

        if file_name in CONFIG_FILES:
            configuration_files.append(file_name)

    return {
        "project_name": repository_path.name,
        "total_files": len(project_files),
        "languages": sorted(languages),
        "readme_present": readme_present,
        "entry_point": entry_point,
        "configuration_files": configuration_files,
        "files": file_paths,
    }