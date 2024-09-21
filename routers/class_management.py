from fastapi import APIRouter, HTTPException
from config.bd import conn
from models.class_management import classes  # Modelo de la tabla 'classes'
from schemas.students_class import ClassStudentSchema
from models.relationships.students_class import students_classes  # Modelo de la tabla intermedia
from models.student import students  # Modelo de la tabla 'students'
from schemas.class_management import ClassSchema
from typing import List
from fastapi.encoders import jsonable_encoder

class_router = APIRouter()

@class_router.get(
    "/classes/{class_id}/students",
    tags=["classes"],
    description="Get a list of students for a specific class",
)
def get_students_in_class(class_id: int):
    # Consulta utilizando SQLAlchemy
    result = conn.execute(students_classes.select().where(students_classes.c.id_clase == class_id)).fetchall()

    # Convertir el resultado en una lista de diccionarios
    students_list = []
    for row in result:
        student_data = {
            "id_student": row[0],  # Acceder por índice de la tupla
            "id_clase": row[1],    # Acceder por índice de la tupla
            # Agrega más campos según las columnas de la tabla
        }
        students_list.append(student_data)

    return jsonable_encoder(students_list)

# Endpoint para añadir estudiantes a una clase
@class_router.post(
    "/classes/{class_id}/students/{student_id}",
    tags=["classes"],
    description="Add a student to a specific class"
)
def add_student_to_class(class_data: ClassStudentSchema):
    # Verificar si el estudiante ya está en la clase
    new_class = {
        "id_clase" : class_data.class_id,
        "id_estudiante" : class_data.student_id
    }

    result = conn.execute(students_classes.insert().values(new_class))
    return conn.execute(students_classes.select().where(students_classes.c.id_estudiante == result.lastrowid)).first()

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
        "subjet": class_data.subjet,
    }
    
    # Inserción usando SQLAlchemy
    result = conn.execute(classes.insert().values(new_class))
    
    # Obtener la clase recién creada
    created_class = conn.execute(classes.select().where(classes.c.id == result.lastrowid)).first()
    
    if not created_class:
        raise HTTPException(status_code=500, detail="Class creation failed")
    
    return created_class

# Endpoint para obtener todas las clases creadas
@class_router.get(
    "/classes/",
    tags=["classes"],
    description="Get a list of all created classes",
    response_model=List[ClassSchema]  # Indica que devuelve una lista de clases
)
def get_all_classes():
    # Consulta todas las clases usando SQLAlchemy
    query = classes.select()
    
    # Ejecuta la consulta y obtiene el resultado
    result = conn.execute(query).fetchall()
    
    if not result:
        raise HTTPException(status_code=404, detail="No classes found")
    
    return result