#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

Base = declarative_base()


class State(Base):
    """State creates a table in Mysql db

       Attribute:
           id(integer)
           name(string)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
