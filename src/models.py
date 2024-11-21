import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(30), nullable=False)
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250), nullable=False)

    def to_dict(self):
        return {}
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    age = Column(Integer)
    eye_color = Column(String(250))

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    persson_id = Column(Integer, ForeignKey("person.id"))
    person=relationship(Person)
    planet_id= Column(Integer, ForeignKey("planet.id"))
    planet=relationship(Planet)
    people_id= Column(Integer, ForeignKey("people.id"))
    people=relationship(People)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
