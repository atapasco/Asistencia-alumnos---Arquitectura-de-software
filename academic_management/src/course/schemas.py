from pydantic import BaseModel
from typing import Optional

class ClassBase(BaseModel):
    name: str
    professor_id: Optional[str]  # El profesor puede ser opcional
    subject_id: Optional[int]     # La materia también puede ser opcional

class ClassCreate(ClassBase):
    name: str
    professor_id: str
    subject_id: int

class ClassUpdate(ClassBase):
    pass  # Para actualizar, puedes usar el mismo modelo

class ClassResponse(ClassBase):
    id: int  # Agregar el ID para la respuesta
