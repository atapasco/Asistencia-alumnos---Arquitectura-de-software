from sqlalchemy import Column, Integer, ForeignKey, Date, String, Table
from database import meta, engine

attendance = Table(
    "attendance",
    meta,
    Column("id", Integer, primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id")), 
    Column("class_id", Integer, ForeignKey("classes.id")),  
    Column("date", Date), 
    Column("status", String(10)) 
)
