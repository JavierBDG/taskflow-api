import time
import uuid
import logging
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import tasks, projects

# Configuración del logger interno para registrar stacktraces en el servidor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("taskflow")

app = FastAPI(
    title="TaskFlow API",
    description="API de gestión de tareas y proyectos - Módulo de Desarrollo Backend",
    version="1.0.0"
)


# 1. Configuración de CORSMiddleware
# Permitimos comunicación desde frontend local (Vite/React en puerto 5173)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Process-Time", "X-Request-ID"],
)


# 2. Middleware personalizado: Medición de tiempo de respuesta y X-Request-ID

@app.middleware("http")
def add_process_time_and_request_id(request: Request, call_next):
    start_time = time.perf_counter()
    request_id = str(uuid.uuid4())
    
    response = call_next(request)
    
    process_time = (time.perf_counter() - start_time) * 1000  # Convertir a ms
    response.headers["X-Process-Time"] = f"{process_time:.2f}ms"
    response.headers["X-Request-ID"] = request_id
    
    return response

# 3. Exception Handler Global: Captura de errores no controlados (500)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Registro de error y stacktrace completo únicamente en logs internos
    logger.error(f"Error no controlado en {request.url}: {exc}", exc_info=True)
    
    # Respuesta genérica al cliente sin exponer datos sensibles ni stacktrace
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error_code": "INTERNAL_SERVER_ERROR",
            "error": "Ha ocurrido un error interno en el servidor. Por favor, inténtelo de nuevo más tarde."
        }
    )

# Endpoints globales de salud/sistema
@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}

@app.get("/version", tags=["system"])
def get_version():
    return {"version": "1.0.0", "app_name": "TaskFlow API"}

@app.get("/ping", tags=["system"])
def ping():
    return {"message": "pong"}

# Registro de routers versionados
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(projects.router, prefix="/api/v1")
