from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import ClassCreate, ClassResponse 
from .service import create_class, get_all_classes, get_class_by_id, update_class, delete_class

class_router = APIRouter()

@class_router.get("/classes", tags=["classes"], response_model=List[ClassResponse], description="Get a list of all classes")
def get_classes():
    return get_all_classes()

@class_router.post("/classes", tags=["classes"], response_model=ClassResponse, description="Create a new class")
def create_class_endpoint(class_data: ClassCreate):
    return create_class(class_data)

@class_router.get("/classes/{class_id}", tags=["classes"], response_model=ClassResponse, description="Get a specific class by ID")
def get_class(class_id: int):
    class_data = get_class_by_id(class_id)
    if not class_data:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_data

@class_router.put("/classes/{class_id}", tags=["classes"], response_model=ClassResponse, description="Update a class by ID")
def update_class_endpoint(class_id: int, class_data: ClassCreate):
    updated_class = update_class(class_id, class_data)
    if not updated_class:
        raise HTTPException(status_code=404, detail="Class not found")
    return updated_class

@class_router.delete("/classes/{class_id}", tags=["classes"], description="Delete a class by ID")
def delete_class_endpoint(class_id: int):
    result = delete_class(class_id)
    if not result:
        raise HTTPException(status_code=404, detail="Class not found")
    return {"message": "Class deleted successfully"}