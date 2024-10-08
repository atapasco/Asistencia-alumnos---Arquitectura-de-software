from fastapi import FastAPI
from sqlalchemy import create_engine
from models import Base

app = FastAPI()

DATABASE_URL = "mysql://root:rootpassword@mysql:3306/mydatabase"
engine = create_engine(DATABASE_URL)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito.")

@app.get("/")
def read_root():
    return {"message": "Microservicio para crear tablas en la base de datos"}