# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 18:28:06 2018

@author: Joseph
SqlAlchemy Basics
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

#1 Create an engine
    engine = create_engine('sqlite:///:memory:', echo=False)    #echo=True turns on logging

#1.1 Create all engines    
    Base.metadata.create_all(engine)
    
#2 Create a sessionmaker instance
    Session = sessionmaker()

#3 Binding a session to an engine
    Session.configure(bind=engine)  # Once an engine is available

#3.1 Instantiate tha session
    session = Session()
    
#    print('session: '+str(session.info))
#    print('Session: '+str(Session.object_session))

#4 Adding Tables to our database / Instances of a given class to our session
    ed_user = User(name='ed', fullname='Ed Jones', password='edpassword')
    session.add(ed_user)
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinktsone', password='blah')])

#4.1 Query the session
    what_user = session.query(User).filter_by(name='ed').first()

#4.2 Alter the class    
    ed_user.password = 'f8s7ccs'

#4.3 Query the session to find altered instances
    print(session.dirty)    
    
#4.4 Commit session commeands
    session.commit()    
#5 Issue Commands during a session

   
    
    

    
    
    
