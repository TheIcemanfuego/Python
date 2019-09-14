# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:39:38 2019

@author: V866620
"""

import os
import xlrd
import re

wd = os.getcwd()

vnr = r'(LF)([0-9]{9})'
re_vnr = re.compile(vnr)


INPUT = 'data.txt'

def read_input():
    fname = os.path.join(wd, INPUT)
    
    print(fname)
    if os.path.isfile(fname):
        f = open(fname, 'r+')
        lines = f.readlines()
    
        print(str(lines))
        
        for l in lines:
            print(str(l))
        
        

def read_vnrs(sheet):
    col = sheet.col_values(0)
    #col_index = list(range(0, sheet.nrows))
    
    mapper = {}
    for i in range(0, len(col)):
        if col[i] in mapper:
            mapper[col[i]].append(i)
        else:
            mapper.update({col[i]: [i]})
            
    return mapper
        
    


def open_wb(file):
    if os.path.isfile(fname):  
        xlfile = xlrd.open_workbook(fname)
        sheets = xlfile.sheets()
        ws = {}
        for s in sheets:
            ws.update({s.name: s})
            
    return ws            

if __name__ == "__main__":
    
    fname = os.path.join(wd, "Bearb.xlsx")

    ws = open_wb(fname)

    sh = ws['Files1']
    mapper = read_vnrs(sh)
    
    read_input()
