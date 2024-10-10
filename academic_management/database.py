import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL", "mysql://root:rootpassword@mysql:3306/mydatabase")


engine = create_engine(DATABASE_URL)
meta = MetaData()


SessionLocal = sessionmaker(bind=engine)

try:
    with engine.connect() as conn:
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
