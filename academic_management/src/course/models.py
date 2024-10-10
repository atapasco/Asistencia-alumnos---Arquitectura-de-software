from sqlalchemy import Column, Table, ForeignKey,UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, String
from database import meta
from sqlalchemy.orm import relationship

classes = Table(
    "classes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name",String(255)),
    Column("professor_id", String(12), ForeignKey("professors.id")),
    Column("subject_id", Integer, ForeignKey("subjects.id"))
)