# AI Project Understanding Assistant

An AI-powered backend application that analyzes software repositories and generates beginner-friendly explanations using Google's Gemini AI.

The application accepts a ZIP file containing a software project, analyzes its structure, identifies technologies and architecture, builds an optimized AI context, and generates a detailed explanation of the project.

---

## Features

- Upload any software project as a ZIP file
- Automatic repository extraction
- Repository file reader with intelligent filtering
- Programming language detection
- Framework detection
- Architecture detection
- Entry point detection
- Database detection
- Configuration file detection
- AI prompt generation
- Intelligent project context builder
- Gemini AI integration
- Centralized exception handling
- Global error handling
- Structured logging
- FastAPI backend
- Modular and scalable architecture

---

## Project Structure

```
app/
├── api/
│   ├── endpoints/
│   └── router.py
│
├── core/
│   ├── custom_exceptions.py
│   ├── exception_handlers.py
│   ├── logging.py
│   └── settings.py
│
├── services/
│   ├── ai/
│   │   └── gemini_service.py
│   ├── analyzer.py
│   ├── context_builder.py
│   ├── file_reader.py
│   ├── prompt_builder.py
│   └── upload_service.py
│
├── utils/
│
└── main.py
```

---

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- Pydantic
- Uvicorn
- python-dotenv

---

## Workflow

```
Upload ZIP
     │
     ▼
Save Repository
     │
     ▼
Extract ZIP
     │
     ▼
Read Repository
     │
     ▼
Analyze Project
     │
     ├────────► Project Analysis
     │
     └────────► Context Builder
                    │
                    ▼
             Prompt Builder
                    │
                    ▼
              Gemini AI
                    │
                    ▼
        Beginner-Friendly Explanation
```

---

## API Endpoint

### Upload Repository

```
POST /upload/
```

Request:

- multipart/form-data

Body:

```
file = repository.zip
```

Response:

```json
{
  "analysis": {},
  "explanation": "..."
}
```

---

## Environment Variables

Create a `.env` file.

```
APP_NAME=AI Project Understanding Assistant
APP_VERSION=0.1.0

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/RACHITJAIN0804/AI-Project-Understanding-Assistant.git
```

Go to the project directory

```bash
cd AI-Project-Understanding-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## Current Progress

### Completed

- Repository Upload Service
- Repository Extraction
- Repository Reader
- Repository Analyzer
- Framework Detection
- Architecture Detection
- Project Context Builder
- Prompt Builder
- Gemini AI Integration
- Custom Exceptions
- Global Exception Handling
- Structured Logging

### In Progress

- Intelligent Context Ranking
- Advanced Prompt Engineering
- AI Response Optimization

### Planned

- Conversational Chat with Repository
- Project Flow Visualization
- Dependency Graph
- Code Search
- Semantic Retrieval
- Multi-LLM Support
- Authentication
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Deployment

---

## Future Vision

The goal of this project is to build an AI assistant capable of understanding any software repository and explaining it in a way that helps beginners, students, developers, and recruiters quickly understand unfamiliar codebases.

---

## Author

**Rachit Jain**
