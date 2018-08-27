# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:56:23 2018

@author: joseph
"""

class Gevo():
    
    def __init__(self, name):
        self.name = name        

    def __str__(self):
        #retstr = "Class: "+ str(self.name)
        return "Class: "+ str(self.name)
        #super.__str__()
        
    def __repr__(self):
        return ("Gevo({!r})".format(self.name))
        #super.__repr__()
    

class Zeitmodell():
    
    def __init__(self, name):
        self.name = name        

    def __str__(self):
        #retstr = "Class: "+ str(self.name)
        return "Class: "+ str(self.name)
        #super.__str__()
        
    def __repr__(self):
        return ("Zeitmodell({!r})".format(self.name))            


class Zustand():
    
    def __init__(self, name):
        self.name = name        

    def __str__(self):
        #retstr = "Class: "+ str(self.name)
        return "Class: "+ str(self.name)
        #super.__str__()
        
    def __repr__(self):
        return ("Zustand({!r})".format(self.name))


zustand_list = [
      'PolicyIsInPayoutPhase'
    , 'PolicyIsNotInPayoutPhase'
]

zeitmodell_list = [
      '10014'
    , '10015'
    , '10016'
    , '10017'
    , '10018'
    , '10019'
    , '10020'    
]

if __name__ == "__main__":
    Z = set()
    for z in zustand_list:
        Z.add(Zustand(z))

    ZM = set()
    for zm in zeitmodell_list:
        ZM.add(Zeitmodell(zm))        

    print(Z)
    print(ZM)