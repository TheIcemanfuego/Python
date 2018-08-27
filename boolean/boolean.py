# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:38:01 2018

@author: joseph
"""

#from set import Set
engineers_list = [
      'John'
    , 'Jane'
    , 'Jack'
    , 'Janice'
]

programmers_list = [
      'Jack'
    , 'Sam'
    , 'Susan'
    , 'Janice'
]

managers_list = [
      'Jane'
    , 'Jack'
    , 'Susan'
    , 'Zack'
]

if __name__ == "__main__":
    engineers_set   = set(engineers_list)
    programmers_set = set(programmers_list)
    managers_set    = set(managers_list)
    
    employees = engineers_set | programmers_set | managers_set
    engineering_management = engineers_set & managers_set
    fulltime_management = managers_set - engineers_set - programmers_set
    
    engineers_set.add('Marvin')
    
    print (engineers_set)