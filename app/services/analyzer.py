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


def detect_framework(file_names, project_files):

    if "requirements.txt" in file_names:

        requirements = next(
            (
                f["content"].lower()
                for f in project_files
                if f["name"] == "requirements.txt"
            ),
            "",
        )

        if "fastapi" in requirements:
            return "FastAPI"

        if "flask" in requirements:
            return "Flask"

        if "django" in requirements:
            return "Django"

    if "package.json" in file_names:

        package = next(
            (
                f["content"].lower()
                for f in project_files
                if f["name"] == "package.json"
            ),
            "",
        )

        if "react" in package:
            return "React"

        if "vue" in package:
            return "Vue"

        if "angular" in package:
            return "Angular"

        if "express" in package:
            return "Express.js"

    if "pom.xml" in file_names:
        return "Spring Boot"

    return "Unknown"


def detect_architecture(file_paths):

    folders = {
        Path(path).parts[0]
        for path in file_paths
        if len(Path(path).parts) > 1
    }

    expected = {
        "api",
        "routers",
        "services",
        "models",
        "schemas",
        "core",
        "database",
    }

    if len(expected.intersection(folders)) >= 3:
        return "Layered Architecture"

    return "Unknown"


def detect_database(project_files):

    content = "\n".join(
        project_file["content"].lower()
        for project_file in project_files
    )

    if "sqlalchemy" in content:
        return "SQLAlchemy"

    if "sqlite" in content:
        return "SQLite"

    if "postgresql" in content:
        return "PostgreSQL"

    if "mysql" in content:
        return "MySQL"

    return "Not Detected"


def estimate_project_size(total_files):

    if total_files < 20:
        return "Small"

    if total_files < 100:
        return "Medium"

    return "Large"


def analyze_repository(repository_path: Path, project_files: list):

    languages = set()

    file_paths = []

    readme_present = False

    entry_point = None

    configuration_files = []

    file_names = []

    for project_file in project_files:

        extension = project_file["extension"]

        if extension in LANGUAGE_MAP:
            languages.add(LANGUAGE_MAP[extension])

        file_name = project_file["name"]

        file_names.append(file_name)

        file_paths.append(project_file["path"])

        if file_name.lower().startswith("readme"):
            readme_present = True

        if file_name in ENTRY_FILES and entry_point is None:
            entry_point = project_file["path"]

        if file_name in CONFIG_FILES:
            configuration_files.append(file_name)

    framework = detect_framework(
        file_names,
        project_files,
    )

    architecture = detect_architecture(file_paths)

    database = detect_database(project_files)

    return {
        "project_name": repository_path.name,
        "total_files": len(project_files),
        "languages": sorted(languages),
        "framework": framework,
        "architecture": architecture,
        "database": database,
        "project_size": estimate_project_size(len(project_files)),
        "readme_present": readme_present,
        "entry_point": entry_point,
        "configuration_files": configuration_files,
        "files": file_paths,
    }