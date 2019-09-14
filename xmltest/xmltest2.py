# -*- coding: utf-8 -*-

import os
import xmlschema
#import regex
from xml.etree import ElementTree as ET
from pprint import pprint
from datetime import datetime


#[0-9]{8}

folder = "C:/Users/Joseph/Documents/data/xml"
fokoxsdfile = "C:/Users/Joseph/Documents/data/xml/fondskostenklasse.xsd"

fokofile = "C:/Users/Joseph/Documents/data/xml/fondskostenklasse-ERGO_fokokl_1527.xml"



def update_xml(xmlfile, xsd):
    
    
    if os.path.isfile(xmlfile) and xsd.is_valid(xmlfile):
        xt = ET.parse(xmlfile)
        
    root = xt.getroot()
    
    for child in root:
        print(str(child.tag)+': '+ str(child.attrib['guel_ab']))


def validate_all_xml(xmlpath, schemafile):

    valid_xml    = []
    invalid_xml  = []
    schema = xmlschema.XMLSchema(schemafile)   
       
    if os.path.isdir(xmlpath):
        print('Validating using schema: '+ str(os.path.basename(schemafile)))
        for f in os.listdir(xmlpath):
            if f.endswith('.xml'):
                try:
                    if not schema.is_valid(os.path.join(xmlpath,f)):
                        raise xmlschema.XMLSchemaValidationError
                    else:
                        valid_xml.append(f)
                except :
                    print('Validation failed: ' + str(f))
                    invalid_xml.append(f)
                finally:
                    pass
                    
                    
        print('Valid XML: ' + str(len(valid_xml)))
        print('Invalid XML: ' + str(len(invalid_xml)))

if __name__ == "__main__":
    
    
    validate_all_xml(folder, fokoxsdfile)
#    update_xml(fokofile, xmlschema.XMLSchema(fokoxsdfile))    
    
    
#    print(schema.notations)
#    print(schema.types)
#    print(schema.elements)
#    print(schema.attributes)
#    print(schema.substitution_groups)
#    print(schema.groups)
#    print(schema.attribute_groups)
    
#    print(schema.is_valid(fokofile))    
