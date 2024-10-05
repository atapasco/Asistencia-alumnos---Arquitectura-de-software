from fastapi import APIRouter, HTTPException
from typing import List
from starlette.status import HTTP_404_NOT_FOUND
from schemas.subject import SubjectSchema
from service.subject_service import get_all_subjects, create_new_subject

subject_router = APIRouter()

@subject_router.get(
    "/subjects",
    tags=["subjects"],
    response_model=List[SubjectSchema],
    description="Get a list of all subjects",
)
def get_subjects():
    subjects = get_all_subjects()
    if not subjects:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No subjects found")
    return subjects

@subject_router.post(
    "/subject_post", 
    tags=["subjects"], 
    response_model=SubjectSchema, 
    description="Create a new subject"
)
def create_subject(subject: SubjectSchema):
    return create_new_subject(subject)