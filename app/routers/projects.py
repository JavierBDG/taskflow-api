from datetime import datetime
from fastapi import APIRouter, status
from app.schemas import ProjectCreate, ProjectRead

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)


@router.post(
    "",
    response_model=ProjectRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo proyecto",
    description="Recibe un schema ProjectCreate, valida sus datos mediante Pydantic y retorna un ProjectRead simulado."
)
def create_project(project_in: ProjectCreate):
    return ProjectRead(
        id=1,
        name=project_in.name,
        description=project_in.description,
        created_at=datetime.now()
    )
