from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

Base = declarative_base()

class Bloque_BD(Base):

    __tablename__ = "bloque_BD"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Integer)
    fecha = Column(DateTime)
    juzgado = Column(String)
    asignado_a = Column(String)

    def __init__(self, cantidad, fecha, juzgado, asignado_a):
        self.cantidad = cantidad
        self.fecha = fecha
        self.juzgado = juzgado
        self.asignado_a = asignado_a

    def info(self):
        return self.cantidad, self.fecha, self.juzgado, self.asignado_a