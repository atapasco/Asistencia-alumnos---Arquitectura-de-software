from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.bd import meta, engine

classes = Table(
    "classes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name",String(255)),
    Column("professor", String(12), ForeignKey("professors.id")),
    Column("subjet", Integer, ForeignKey("subjects.id")),
    
)

meta.create_all(engine)
