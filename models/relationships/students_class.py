from sqlalchemy import Column, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String
from config.bd import meta, engine

students_classes = Table(
    "students_classes",
    meta,
    Column("id_clase", Integer, ForeignKey("classes.id")),
    Column("id_estudiante", Integer, ForeignKey("students.id")),
    PrimaryKeyConstraint("id_estudiante", "id_clase")  # Llave primaria compuesta
)

meta.create_all(engine) 