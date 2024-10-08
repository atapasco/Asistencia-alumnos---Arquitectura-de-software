from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    email = Column(String(255), primary_key=True)
    password = Column(String(255))
    role = Column(Integer)

class Attendance(Base):
    __tablename__ = 'attendance'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    date = Column(Date)
    status = Column(String(10))

class Professor(Base):
    __tablename__ = 'professors'
    
    id = Column(String(12), primary_key=True)
    user_email = Column(String(255), ForeignKey("users.email"), unique=True)
    name = Column(String(255))
    birth_date = Column(Date)

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    user_email = Column(String(255), ForeignKey("users.email"))
    name = Column(String(255))
    birth_date = Column(Date)
    grade = Column(Integer)

class Class(Base):
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    subject_id = Column(Integer, ForeignKey("subjects.id"))  