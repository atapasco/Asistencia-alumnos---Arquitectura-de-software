from sqlalchemy import Column, Integer, ForeignKey, String, Date, Table
from config.bd import meta, engine

professors = Table(
    "professors",
    meta,
    Column("id", String(12), primary_key=True),
    Column("user_email", String(255), ForeignKey("users.email"), unique=True),
    Column("name", String(255)),
    Column("birth_date", Date)
)

meta.create_all(engine)