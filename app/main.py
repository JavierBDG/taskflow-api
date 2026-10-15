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
