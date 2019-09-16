# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:25:39 2019

@author: Joseph
"""

import datetime
import workday as W

#List of Queries to run on first workday
DAILY = [
  'VAAD0001'
, 'EAAD0013'
, 'VAAD0008'
]


#List of Queries to run on first workday
FIRSTWORKDAY = [
  'VAAD0001'
, 'LAAD0013'
, 'LAAD0008'
]


#List of Queries to run on Midmonth workday
MIDWORKDAY = [
  'LAAD0009'
, 'VAAD0013'
, 'EAAD0013'
, 'AAAD0008'
]


#List of Queries to run on last workday
LASTWORKDAY = [
  'LAAD0001'
, 'AAAD0013'
, 'AAAD0008'
]


WEEKLY = [
  'UAAD0002'
, 'VAAD0012'
, 'WAAD0002'       
]

BIWEEKLY = [
  'RAAD0002'
, 'SAAD0012'
, 'TAAD0002'       
]


def queriesToday(d):
    w = W.Workdays(d.month, d.year)
    wl = W.Workdays2List(w)
    
    wknr = d.isocalendar()[1]
    
    TODAY = []    
    
    if d == wl[0]:
        TODAY += FIRSTWORKDAY
        
    if d == wl[1]:
        TODAY += MIDWORKDAY
        
    if d == wl[2]:
        TODAY += LASTWORKDAY
        
    if d.isoweekday() == 1:
        TODAY += WEEKLY
        
    if d.isoweekday() == 1 and wknr % 2 == 0:
        TODAY += BIWEEKLY
        
    TODAY += DAILY
    return set(TODAY)
        

def copy2Runlib(queries):
    
    for q in queries:
        #execute remote copy command
        pass
    

if __name__ == "__main__":
    d = datetime.datetime.now().date()
    t = datetime.date(2019, 9, 30)
    #wknr = d.isocalendar()[1]
    
    r = queriesToday(t)
    
    print(str(r))