from fastapi import FastAPI

app = FastAPI(
    title="AI Project Understanding Assistant",
    description="Backend API for analyzing and understanding software projects.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "Welcome to AI Project Understanding Assistant"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }