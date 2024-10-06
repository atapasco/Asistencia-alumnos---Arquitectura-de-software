from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql://root:rootpassword@localhost:3306/mydatabase")

meta = MetaData()

conn = engine.connect()