from datetime import datetime
from fastapi import APIRouter, status
from app.schemas import TaskCreate, TaskRead

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva tarea",
    description="Recibe un schema TaskCreate, valida los datos con Pydantic y retorna una TaskRead simulada."
)
def create_task(task_in: TaskCreate):
    return TaskRead(
        id=1,
        title=task_in.title,
        description=task_in.description,
        project_id=task_in.project_id,
        completed=False,
        created_at=datetime.now()
    )


# Endpoint de prueba 
@router.get("/error-test", summary="Provocar un error no controlado de prueba")
def trigger_error():
    """Fuerza un error imprevisto (división por cero) para probar el Exception Handler."""
    return 1 / 0
