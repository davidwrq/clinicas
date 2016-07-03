from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_clinicas_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Clinicas(DeclarativeBase):
    """Sqlalchemy dentists model"""
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    rubro = Column('rubro', String)
    rut = Column('rut', String, nullable=True)
    direccion = Column('direccion', String)
    comuna = Column('comuna', String)
    ciudad = Column('ciudad', String)
    razon_social = Column('razon_social', String)
    telefono = Column('telefono', String, nullable=True)
    contacto = Column('contacto', String, nullable=True)
    rol = Column('rol', String, nullable=True)
    nombre_de_fantasia = Column('nombre_de_fantasia', String)
    sitio_web = Column('sitio_web', String, nullable=True)
    mail = Column('mail', String, nullable=True)
    facebook = Column('facebook', String, nullable=True)
