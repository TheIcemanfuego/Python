# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 18:28:06 2018

@author: Joseph
SqlAlchemy Basics
"""


from sqlalchemy import create_engine
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base
Base = declarative_base()

# Create a new class by extending the declarative base class
class User(Base):
    # required identifier __tablename__
    __tablename__ = 'users'    

    # A table requires at least 1 primary key column
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True)
    
    name     = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    
    def __repr__(self):
        return "<User(name)'%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

if __name__ == "__main__":

# Create an engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    
    Base.metadata.create_all(engine)
    print(User.__table__)
    
    

    
    
    