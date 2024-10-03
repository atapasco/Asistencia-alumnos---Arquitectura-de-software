from sqlalchemy import Column, Integer, String, Table
from config.bd import meta, engine


subjects = Table(
    "subjects",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),  
    Column("description", String(255)), 
)

meta.create_all(engine)