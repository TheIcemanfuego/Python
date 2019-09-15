# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:41:13 2019

@author: Joseph
"""
# Workday Module
#
# A Workday is a weekday that is not a holiday
# 
# Of particular interest are the following workdays:
#
# 1. First workday of the month.
# 2. last workday of the month.
# 3. MidMonthWorkday: The first workday after the 14th of every month.


import datetime
import calendar
import pandas as pd

import holidays as H


#HOLS = H.defineHolidays(2019)
#HOLSPD = H.Holidays2DataFrame(HOLS)

HOLS = {}
HOLSL = []

WORKDAYS = {}

def FirstWorkday(month, year):    

    #add a day to the first day of the month
    d = datetime.date(year, month, 1)
    found = False
    
    while found == False:
        if d.isoweekday() > 5:
            d += datetime.timedelta(days=1)
        elif d in HOLSL:
            d += datetime.timedelta(days=1)
        else:
            found = True
            return d
        
    
def LastWorkday(month, year):    
    
    r = calendar.monthrange(year, month)
    
    #subtract a day from the last day of the month
    d = datetime.date(year, month, r[1])
    found = False
    
    while found == False:
        if d.isoweekday() > 5:
            d -= datetime.timedelta(days=1)
        elif d in HOLSL:
            d -= datetime.timedelta(days=1)
        else:
            found = True
            return d
    
    
def MidMonthWorkday(month, year): 


    #add a day to the fifteenth day of the month
    d = datetime.date(year, month, 15)
    found = False
    
    while found == False:
        if d.isoweekday() > 5:
            d += datetime.timedelta(days=1)
        elif d in HOLSL:
            d += datetime.timedelta(days=1)
        else:
            found = True
            return d


def Workdays(month, year):
    
    if len(WORKDAYS) == 0:
        WORKDAYS.update({'FirstWorkday': FirstWorkday(month, year)})
        WORKDAYS.update({'MidMonthWorkday': MidMonthWorkday(month, year)})
        WORKDAYS.update({'LastWorkday': LastWorkday(month, year)})
    
    return WORKDAYS
        
def Workdays2DataFrame(W):
    
    w = []
    d = []
    
    for k, v in W.items():
        w.append(k)
        d.append(v)
    
    data = {'Workday' : w, 'Date': d}
    return pd.DataFrame.from_dict(data)


def Workdays2List(W):
    p = Workdays2DataFrame(W)
    
    return p['Date'].tolist()
    

if __name__ == "__main__":

    
    #print(H.Holidays2DataFrame(H.defineHolidays(2019)))
    today = datetime.datetime.now() 
    HOLS = H.defineHolidays(2019)
    HOLSL = H.Holidays2List(HOLS)

    w = Workdays(12, 2019)
    wpd = Workdays2DataFrame(w)
    wl = Workdays2List(w)
    
    print(wpd)