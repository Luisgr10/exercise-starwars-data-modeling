import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Usuario (Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(Date, nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favoritos_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('Usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('Planetas.planeta_id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('Personajes.planeta_id'), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    planeta_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)

class Personajes (Base):
    __tablename__ = 'personajes'
    planeta_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
