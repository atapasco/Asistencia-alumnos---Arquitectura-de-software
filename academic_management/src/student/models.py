from sqlalchemy import Column, Integer, ForeignKey, String, Date, Table
from database import meta, engine

students = Table(
    "students",
    meta,
    Column("id", Integer, primary_key=True),
    Column("user_email", String(255), ForeignKey("users.email")),
    Column("name", String(255)),
    Column("birth_date", Date),
    Column("grade", Integer),
)
