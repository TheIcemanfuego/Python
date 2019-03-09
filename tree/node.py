# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:19:59 2018

@author: Joseph
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from abc import ABCMeta, abstractmethod, abstractproperty

CLASSES = [
    'produkt'
    , 'z_produkt_tp'
    , 'tpd'
    , 'zeitmodell'
    , 'tp'
    , 'kasys'
    , 'ttpd'
    , 'z_ttpd_rps'
    , 'z_ttpd_modvorg'
    , 'tf'
    , 'z_tpr'
    , 'z_tpr'
]


ASSOZIATIV = [
    'z_produkt_tp'
    , 'z_ttpd_rps'
    , 'z_ttpd_modvorg'
    , 'z_tpr'
    , 'z_tpr'
]


class Model():
    
    def __init__(self):
        self._classlist = {
                'produkt' : ['z_produkt_tp', 'tpd']
              , 'z_produkt_tp' : ['tp']
              , 'tpd' : ['ttpd']
                }
        self._relations = None
    
    def __repr__():
        pass
        
    def __str__():
        pass
        
MODEL = Model()

class Node(metaclass = ABCMeta):
    
    
    _children  = []             # List of instances of classe with edges originating drom this node    
    _parents   = []             # List instances of classes with edges ending in this node
    _relations = []             #
    #_isAssoziativ = None

        
    def __init__(self, name=None, typ=None):
        self._type = typ
        self._name = name        
        self._isAssoziativ = self.set_isAssoziativ()
        
    def __repr__(self):
        s = "Node({0!r}, {1!r})".format(self._name, self._type)
        return s
    
    def __str__(self):
        s = "Class: {0!r}\nName: {1!r}\nChildren: {2!r}\nAssoziativ: {3!r}".format(\
                    self._type, self._name, len(self._children), self._isAssoziativ)
        return s
    
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    @abstractmethod
    def attach(self, node):
        #checks
        #p = model
        if node._type in MODEL._classlist[self._type]:
            self._children.append(node)
        else:
            print('The Attachment of nodetype : {0!r} to nodetype {1!r} is not allowed'.format(node._type, self._type))
        
        #self._relations
        
    def delete(self):
        pass
    
    def cascadeDelete(self, node):
        pass
    
    def getAddress(self):
        pass
    
    def printChildren(self):
        print('Printing Children:')
        for e in self._children:
            print("------------------")
            print(e)
        
    def set_isAssoziativ(self):
        return (self._type in ASSOZIATIV)
    

class Produkt(Node):
    
    def __init__(self, name=None):
        self._type = 'produkt'
        self._name = name
        self._isAssoziativ = super().set_isAssoziativ()
        
    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

    def attach(self, node):
        super().attach(node)


class Z_produkt_tp(Node):
    
    def __init__(self, name=None):
        self._type = 'z_produkt_tp'
        self._name = name
        self._isAssoziativ = super().set_isAssoziativ()
    
    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

    def attach(self):
        pass

if __name__ == "__main__":
    a = Produkt(name='ERGO_FFR_13')
    b = Z_produkt_tp()
    c = Produkt(name = 'ERGO_FFRG_DV_15')
    
    a.attach(b)
    a.attach(c)
    
    a.printChildren()
    
    d = Produkt(name='ERGO_FFRG_13')
    
    #print(c)