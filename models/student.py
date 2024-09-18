from sqlalchemy import Column, Integer, ForeignKey, String, Date, Table
from config.bd import meta, engine

students = Table(
    "students",
    meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("name", String(255)),
    Column("birth_date", Date),
    Column("grade", Integer),
)

meta.create_all(engine)