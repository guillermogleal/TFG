from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

Base = declarative_base()

class Letrado_BD(Base):

    __tablename__ = "letrado_BD"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    jefe = Column(Boolean)

    def __init__(self, nombre, jefe):
        self.nombre =nombre
        self.jefe = jefe

    def info(self):
        return self.nombre, self.jefe