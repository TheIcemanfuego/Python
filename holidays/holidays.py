# -*- coding: utf-8 -*-
#Holiday Module
#
# 1. There are different types of holidays
#	  i. International holidays
#	 ii. National holidays
#	iii. Regional holidays
#	
# 2. Holidays can be divided into 2 types
#	 i. Regular holidays whose date can be ascertained by a given algorithm.
#	ii. Irregular holidays whose dates must be explicitly ascertained.
	
import datetime
import pandas as pd
	
HOLIDAYS = {
	'IH' : { 'IHR' : [], 'IHI' : []}
	
,	'NH' : { 'NHR' : [], 'NHI' : []}

,	'RH' : { 'RHR' : [], 'RHI' : []}
}

# Regular International holidays
IHR = {
	'New Years Day' : '01-01-JJJJ'
, 	'Labour Day'    : '01-05-JJJJ'
,   'Christmas Eve' : '24-12-JJJJ'
,   'Christmas Day' : '25-12-JJJJ'
,   'Boxing Day'    : '26-12-JJJJ'
,   "New Year's Eve": '31-12-JJJJ'
}

# Irregular International holidays
IHI = {
	'Good Friday' : ''
,	'Easter Monday' : ''
}


# Regular National holidays
NHR = {
	'Tag der Deutschen Einheit'	: '03-10-JJJJ'
}


# Irregular National holidays
NHI = {
	'Christi Himmelfahrt' : ''
,	'Pfingstmontag' : ''	
}

# Regular regional holidays
RHR = {
	'Allerheiligen' : '01-11-JJJJ'
}

# Irregular regional holidays
RHI = {
	'Fronleichnahm' : ''
,   'Rosenmontag' : ''    
}


Order = []


def computus(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    
    return datetime.date(year, month, day)
        



# Regular holidays
def defineRegularHolidays(year):
    
    for b in [IHR, NHR, RHR]:
        for k, v in b.items():
            b[k] = b[k].replace('JJJJ', str(year))
            b[k] = datetime.datetime.strptime(b[k], '%d-%m-%Y').date()
           


def defineIrregularHolidays(year):
    easter = computus(year)
    
    IHI['Good Friday']   = easter - datetime.timedelta(days=2)
    IHI['Easter Monday'] = easter + datetime.timedelta(days=1)

    NHI['Christi Himmelfahrt'] = easter + datetime.timedelta(days=40)
    NHI['Pfingstmontag']      = easter + datetime.timedelta(days=51)
    
    RHI['Fronleichnahm'] = easter + datetime.timedelta(days=60)
    RHI['Rosenmontag'] = easter - datetime.timedelta(days=48)

def defineHolidays(year):
    
    
    defineRegularHolidays(year)
    defineIrregularHolidays(year)
# Irregular holidays
    
            
    
    HOLIDAYS['IH']['IHR'] = IHR
    HOLIDAYS['IH']['IHI'] = IHI
    HOLIDAYS['NH']['NHR'] = NHR
    HOLIDAYS['NH']['NHI'] = NHI
    HOLIDAYS['RH']['RHR'] = RHR
    HOLIDAYS['RH']['RHI'] = RHI
    
    return HOLIDAYS
    

def Holidays2DataFrame(H):
    h = []
    d = []
    
    for k1, v1 in H.items():
        for k2, v2 in v1.items():
            for k, v in v2.items():
                h.append(k)
                d.append(v)
    
    data = {'Holiday' : h, 'Date': d}
    return pd.DataFrame.from_dict(data)
    


def Holidays2List(H):
    p = Holidays2DataFrame(H)
    
    return p['Date'].tolist()

if __name__ == "__main__":
    #y = datetime.date(('01-01-2019')

    H  = defineHolidays(2019)
    HP = Holidays2DataFrame(H)
    
    print(HP.sort_values('Date'))
    
#    y = datetime.datetime.now()
#    print("Happy New Years! It's :"+y.strftime('%Y'))
    
