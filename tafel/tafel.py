# -*- coding: utf-8 -*-
"""
Created on Tue May  1 02:11:21 2018

@author: 
"""

import os, re

import numpy as np
from matplotlib import pyplot as plt

class TableReader():
    
    def __init__(self, path):
        self.tablesPath = None
        self.tables = {}

        self._initialize(path)
        
    def _initialize(self, path):
        # Input validation
        if not isinstance(path, str):
            raise TypeError("{0} is not a string!".format(path))
        elif not os.path.isdir(path):
            raise AssertionError("{0} is not a valid directory!".format(path))
        
        try:
            for f in os.listdir(path):
                filename, file_extension = os.path.splitext(f)
                if os.path.isfile(f) and str.lower(file_extension) == ".csv":
                    with open(f, newline='') as file:
                        lines = file.readlines()
                        data = {}
                        x  = []
                        qx = []
                        lx = []
                        Dx = []
                        Nx = []
                        Sx = []
                        
                        T = None
                        for row in lines:
                            fields = row.split(',')
                            if not fields[0] in ['x', 'y']:
                         
                                x.append(int(fields[0]))
                                qx.append(float(fields[1]))
                                lx.append(float(fields[2]))
                                Dx.append(float(fields[3]))
                                Nx.append(float(fields[4]))
                                Sx.append(float(fields[5]))
                                
                                data.update({str(fields[0]): fields[1:len(fields)-1]})
                       
                        T = Table(str(filename), x, qx, lx, Dx, Nx, Sx, data)
                    self.tables.update({str(filename): T})
                            
                    
        except Exception as exception:
            raise Exception("There was an Exception!", exception.args)



                
    
    
    def getTable(self, name):        
        if not isinstance(name, str):
            raise TypeError("{0} is not a string!".format(name))
        if not name in self.tables.keys():
            raise Exception("Table {0} was not found!".format(name))
            
        return self.tables[name]


    
class Table():
    
    def __init__(self, name, x, qx, lx, Dx, Nx, Sx, data):
        self.name = name
        self.x  = x
        self.qx = qx
        self.lx = lx
        self.Dx = Dx
        self.Nx = Nx
        self.Sx = Sx
        self.data = data
    
    def setVariables(self):
        pass
    
    
    def q(self, x):
        return self.qx[x]

    def l(self, x):
        return self.lx[x]

    def D(self, x):
        return self.Dx[x]
    
    def N(self, x):
        return self.Nx[x]
    
    def S(self, x):
        return self.Sx[x]
    

    def graph(self):


        ax1 = plt.subplot(321)
        ax1.plot(self.x, self.qx)
        ax1.set_title('q_x')
        
        ax1 = plt.subplot(322)
        ax1.plot(self.x, self.lx)
        ax1.set_title('l_x')
        
        ax1 = plt.subplot(323)
        ax1.plot(self.x, self.Dx)
        ax1.set_title('D_x')
        
        ax1 = plt.subplot(324)
        ax1.plot(self.x, self.Nx)
        ax1.set_title('N_x')
        
        ax1 = plt.subplot(313)
        ax1.plot(self.x, self.Sx)
        ax1.set_title('S_x')
        
        #print("x: "+str(x))
        #print("y: "+str(y))
        #plt.plot(x, y)
#        plt.subplot(2, 3, 1)
#        plt.subplot(2, 3, 3)
#        plt.subplot(2, 3, 4)
        #plt.subplot(2, 3, 4)
        plt.show()
        
t = "  const static double EL2014[122][55][10] = {"
s = "const static double"


#Regular exoressions
re_keyword = re.compile(r"(const)\s+(static)\s+(double)")
re_dim = re.compile(r"(\[([0-9]+)\])+")






if __name__ == "__main__":
    #m = re_keyword.search(s)
#    m = re_dim.search(t)
#    if m:
#        print("0: "+str(m.group(0)))
#        print("1: "+str(m.group(1)))
#        print("2: "+str(m.group(2)))
#        #print("3: "+str(m.group(3)))
#    else:
#        print("false")
    
    tables = TableReader("C:\\Users\\Joseph\\Documents\\Programming\\Python\\tafel")
    
    t1 = tables.getTable('DAV2008M')
    t1.graph()
    
    t2 = tables.getTable('DAV2008F')
    t2.graph()
    
    
    