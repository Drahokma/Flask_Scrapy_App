import string
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

from .settings import DATABASE_URL

def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(DATABASE_URL)


def create_items_table(engine: Engine):
    """
    Create the PropertyScrapItems table
    """
    DeclarativeBase.metadata.create_all(engine)


class Items(DeclarativeBase):
    """
    Defines the items model
    """

    __tablename__ = "items"

    url = Column("url", String, primary_key=True)
    name = Column("name", String)
    locality = Column("locality", String)