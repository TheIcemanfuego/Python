# -*- coding: utf-8 -*-
"""
Created on Tue May  1 02:11:21 2018

@author: 
"""

import os, re


t = "  const static double EL2014[122][55][10] = {"
s = "const static double"

#Regular exoressions
re_keyword = re.compile(r"(const)\s+(static)\s+(double)")
re_dim = re.compile(r"(\[([0-9]+)\])+")






if __name__ == "__main__":
    #m = re_keyword.search(s)
    m = re_dim.search(t)
    if m:
        print("0: "+str(m.group(0)))
        print("1: "+str(m.group(1)))
        print("2: "+str(m.group(2)))
        #print("3: "+str(m.group(3)))
    else:
        print("false")
    
    
