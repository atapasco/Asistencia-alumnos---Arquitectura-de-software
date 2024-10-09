import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Cargar la cadena de conexión desde una variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://root:rootpassword@mysql:3306/mydatabase")

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL)
meta = MetaData()

# Crear una clase de sesión local
SessionLocal = sessionmaker(bind=engine)

try:
    # Probar la conexión
    with engine.connect() as conn:
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
