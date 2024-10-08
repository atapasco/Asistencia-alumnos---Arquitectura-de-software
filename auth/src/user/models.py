from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from database import meta, engine

users = Table(
    "users",
    meta,
    Column("email", String(255),primary_key=True),
    Column("password", String(255)),
    Column("role", Integer()),
)

