import os
from sqlalchemy import create_engine, MetaData

# Cargar la cadena de conexión desde una variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://root:rootpassword@mysql:3306/mydatabase")

engine = create_engine(DATABASE_URL)
meta = MetaData()

try:
    # Usar el bloque 'with' para manejar automáticamente el cierre de conexión
    with engine.connect() as conn:
        # Aquí puedes realizar operaciones con la conexión
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")