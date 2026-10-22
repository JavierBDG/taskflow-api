from fastapi import FastAPI
from app.routers import tasks, projects

app = FastAPI(
    title="TaskFlow API",
    description="API de gestión de tareas y proyectos - Módulo de Desarrollo Backend",
    version="1.0.0"
)

# Endpoints globales de salud y sistema
@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}


@app.get("/version", tags=["system"])
def get_version():
    return {"version": "1.0.0", "app_name": "TaskFlow API"}


@app.get("/ping", tags=["system"])
def ping():
    return {"message": "pong"}


# Registro modular de routers con versionado de API (/api/v1)
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(projects.router, prefix="/api/v1")
