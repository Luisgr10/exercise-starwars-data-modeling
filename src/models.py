import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(Date, nullable=False)
    favoritos = relationship('Favoritos', back_populates='usuario')

class Favoritos(Base):
    __tablename__ = 'favoritos'
    favoritos_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planetas.planeta_id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personajes.planeta_id'), nullable=False)
    usuario = relationship('Usuario', back_populates='favoritos')

class Planetas(Base):
    __tablename__ = 'planetas'
    planeta_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    favoritos = relationship('Favoritos', back_populates='planeta')

class Personajes(Base):
    __tablename__ = 'personajes'
    personaje_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    favoritos = relationship('Favoritos', back_populates='personaje')

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
