from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict



# SCHEMAS DE PROJECT


class ProjectCreate(BaseModel):
    """Schema de entrada para crear un Proyecto."""
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre del proyecto (entre 1 y 100 caracteres)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Descripción opcional del proyecto (máximo 500 caracteres)"
    )


class ProjectRead(ProjectCreate):
    """Schema de salida al leer un Proyecto."""
    id: int = Field(..., gt=0, description="Identificador único del proyecto")
    created_at: datetime = Field(..., description="Fecha y hora de creación")

    model_config = ConfigDict(from_attributes=True)



# SCHEMAS DE TASK


class TaskCreate(BaseModel):
    """Schema de entrada para crear una Tarea."""
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Título de la tarea (obligatorio, entre 1 y 100 caracteres)"
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Descripción opcional de la tarea (máximo 500 caracteres)"
    )
    project_id: int = Field(
        ...,
        gt=0,
        description="ID del proyecto asociado a esta tarea"
    )


class TaskRead(TaskCreate):
    """Schema de salida al leer una Tarea."""
    id: int = Field(..., gt=0, description="Identificador único de la tarea")
    completed: bool = Field(False, description="Estado de realización de la tarea")
    created_at: datetime = Field(..., description="Fecha y hora de creación")

    model_config = ConfigDict(from_attributes=True)
