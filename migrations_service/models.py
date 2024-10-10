from sqlalchemy import Column, Integer, String, ForeignKey, Date, UniqueConstraint, Index
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    professor_id = Column(String(12), ForeignKey("professors.id"), nullable=False)

    subject = relationship("Subject", back_populates="classes")
    professor = relationship("Professor", back_populates="classes")
    
    __table_args__ = (UniqueConstraint('name', 'subject_id', name='uq_class_name_subject'),)

class User(Base):
    __tablename__ = 'users'

    email = Column(String(255), primary_key=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Integer, nullable=False)
    
    professor = relationship("Professor", back_populates="user", uselist=False)
    student = relationship("Student", back_populates="user", uselist=False)

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)

    student = relationship("Student", back_populates="attendance")
    class_ = relationship("Class", back_populates="attendance")

    __table_args__ = (Index('ix_attendance_student_class', 'student_id', 'class_id'),)

class Professor(Base):
    __tablename__ = 'professors'

    id = Column(String(12), primary_key=True, index=True, nullable=False)
    user_email = Column(String(255), ForeignKey("users.email"), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)

    user = relationship("User", back_populates="professor")
    classes = relationship("Class", back_populates="professor")

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))

    classes = relationship("Class", back_populates="subject")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(255), ForeignKey("users.email"), nullable=False)
    name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)
    grade = Column(Integer, nullable=False)

    user = relationship("User", back_populates="student")
    attendance = relationship("Attendance", back_populates="student")