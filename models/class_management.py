from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.bd import meta, engine

classes = Table(
    "classes",
    meta,
    Column("id", String(5), primary_key=True),
    Column("name",String(255)),
    Column("professor", Integer, ForeignKey("professors.id")),
    Column("subjet", Integer, ForeignKey("subjects.id")),
    
)

meta.create_all(engine)
