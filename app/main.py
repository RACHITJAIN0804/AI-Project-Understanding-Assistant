from fastapi import FastAPI
from app.core.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }       