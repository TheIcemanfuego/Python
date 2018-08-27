# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:52:37 2018

@author: joseph
"""
import xml.etree.ElementTree as ET

def read_from_root(root):
    
    for child in root:
        print("{!r}: {!r}".format(child.tag, child.attrib))

if __name__ == "__main__":
    tree = ET.parse('countries.xml')
    root = tree.getroot()
    
    print(root.tag)
    print(root.attrib)
    read_from_root(root)