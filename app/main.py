from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="TaskFlow API",
    description="API para la gestión de tareas e integración de servicios.",
    version="1.0.0",
)


class HealthResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str
    app_name: str


class PingResponse(BaseModel):
    message: str


@app.get("/health", response_model=HealthResponse)
def get_health():
    return {"status": "ok"}


@app.get("/version", response_model=VersionResponse)
def get_version():
    return {"version": app.version, "app_name": app.title}


@app.get("/ping", response_model=PingResponse)
def get_ping():
    return {"message": "pong"}

from datetime import datetime
from fastapi import FastAPI, status
from app.schemas import TaskCreate, TaskRead

app = FastAPI(
    title="TaskFlow API",
    description="API de gestión de tareas y proyectos - Módulo de Desarrollo Backend",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/version")
def get_version():
    return {"version": "1.0.0", "app_name": "TaskFlow API"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


# Endpoint temporal Práctica 1.2
@app.post(
    "/tasks",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva tarea (simulado)",
    description="Recibe un schema TaskCreate, valida sus datos mediante Pydantic y retorna una TaskRead simulada con ID y fecha de creación."
)
def create_task(task_in: TaskCreate):
    # Simulación de respuesta con datos asignados
    return TaskRead(
        id=1,
        title=task_in.title,
        description=task_in.description,
        project_id=task_in.project_id,
        completed=False,
        created_at=datetime.now()
    )
