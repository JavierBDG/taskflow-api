from fastapi import FastAPI
from pydantic import BaseModel

# Inicialización de la app con metadatos para la documentación Swagger
app = FastAPI(
    title="TaskFlow API",
    description="API para la gestión de tareas e integración de servicios.",
    version="1.0.0",
)


# Modelos Pydantic para validar y estructurar las respuestas (response_model)
class HealthResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str
    app_name: str


class PingResponse(BaseModel):
    message: str


# Endpoints
@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Estado del servicio",
    description="Verifica que la API está operativa.",
)
def get_health():
    return {"status": "ok"}


@app.get(
    "/version",
    response_model=VersionResponse,
    summary="Versión de la API",
    description="Devuelve la versión actual y el nombre del proyecto.",
)
def get_version():
    return {"version": app.version, "app_name": app.title}


@app.get(
    "/ping",
    response_model=PingResponse,
    summary="Prueba de conectividad",
    description="Responde con un 'pong' para verificar latencia y disponibilidad.",
)
def get_ping():
    return {"message": "pong"}