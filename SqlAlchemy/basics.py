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

    



def createDB(dbname):

#1 Create an engine
    engine = create_engine('sqlite:///'+dbname+'.db', echo=True)    #echo=True turns on logging    

#1.1 Create all engines    
    Base.metadata.create_all(engine)

    return engine


def testInsert(engine):
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
        User(name='fred', fullname='Fred Flintsone', password='blah')])

#4.4 Commit session commeands
    session.commit()    
    

def testQuery1(engine):
    Session = sessionmaker()    

    Session.configure(bind=engine)
    session = Session()

    what_user = session.query(User).filter_by(name='ed').first()

    print(what_user)
    
    session.commit()
    
    
def testUpdate1(engine):
    Session = sessionmaker()    

    Session.configure(bind=engine)
    session = Session()

    ed_user = session.query(User).filter_by(name='ed').first()

    ed_user.password = 'f8s7ccs'

#4.3 Query the session to find altered instances
    print(session.dirty)        
    
    session.commit()


    
if __name__ == "__main__":

    engine = createDB('alchemy')
    
    testInsert(engine)
    testQuery1(engine)
    engine.echo = False
    testUpdate1(engine)
    testQuery1(engine)
    
   
    
    

    
    
    
