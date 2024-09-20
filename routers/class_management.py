from fastapi import APIRouter, HTTPException
from config.bd import conn
from models.class_management import classes  # Modelo de la tabla 'classes'
from models.relationships.students_class import students_classes  # Modelo de la tabla intermedia
from models.student import students  # Modelo de la tabla 'students'
from schemas.class_management import ClassSchema
from typing import List

class_router = APIRouter()

# Endpoint para obtener todas las clases y los estudiantes relacionados
@class_router.get(
    "/classes/{class_id}/students",
    tags=["classes"],
    description="Get a list of students for a specific class",
)
def get_students_in_class(class_id: int):
    # Consulta utilizando SQLAlchemy
    query = students.join(students_classes, students.c.id == students_classes.c.id_estudiante) \
                    .select() \
                    .where(students_classes.c.id_clase == class_id)
    
    result = conn.execute(query).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="No students found for this class")
    
    return result

# Endpoint para añadir estudiantes a una clase
@class_router.post(
    "/classes/{class_id}/students/{student_id}",
    tags=["classes"],
    description="Add a student to a specific class"
)
def add_student_to_class(class_id: int, student_id: int):
    # Verificar si el estudiante ya está en la clase
    check_query = students_classes.select().where(
        (students_classes.c.id_estudiante == student_id) & 
        (students_classes.c.id_clase == class_id)
    )
    existing = conn.execute(check_query).fetchone()
    
    if existing:
        raise HTTPException(status_code=400, detail="Student is already in this class")

    # Añadir el estudiante a la clase
    conn.execute(students_classes.insert().values(id_estudiante=student_id, id_clase=class_id))
    
    return {"message": f"Student {student_id} added to class {class_id} successfully"}

# Endpoint para crear una nueva clase
@class_router.post(
    "/classes/",
    tags=["classes"],
    response_model=ClassSchema,
    description="Create a new class"
)
def create_class(class_data: ClassSchema):
    new_class = {
        "id": class_data.id,
        "name": class_data.name,
        "professor": class_data.professor,
        "subject": class_data.subject,
    }
    
    # Inserción usando SQLAlchemy
    result = conn.execute(classes.insert().values(new_class))
    
    # Obtener la clase recién creada
    created_class = conn.execute(classes.select().where(classes.c.id == result.lastrowid)).first()
    
    if not created_class:
        raise HTTPException(status_code=500, detail="Class creation failed")
    
    return created_class