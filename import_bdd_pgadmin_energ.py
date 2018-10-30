#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:38:24 2018

@author: Amelie Motteau
"""
import csv
import psycopg2
import pandas as pd
from datetime import datetime


pgconnect = psycopg2.connect(dbname='bdd_test', host='localhost', port='5432', user='postgres', password='1234')
print('Connection')

pgcursor=pgconnect.cursor()

pgcursor.execute("DROP TABLE IF EXISTS energ_table")
pgcursor.execute("""CREATE TABLE energ_table
                 (DATE float,
                 ENER_RUC_FRST5 float,
                 ENER_RUC_FRST6 float,
                 ENER_RUC_FRST7 float,
                 ENER_RUC_FRST8 float,
                 ENER_RUC_CHST5 float,
                 ENER_RUC_CHST6 float,
                 ENER_RUC_CHST7 float,
                 ENER_RUC_CHST8 float,
                 ENER_RUC_REF float);""")

#
#pgconnect.commit()
#print('Creation DB')
#        
#pgcursor.close()
#pgconnect.close()


file = open('/home/iteis/Documents/PFE_V1/genereate/listcomplete.csv', 'r')
try:
    reader = csv.reader(file)
    next(reader)
    print('read csv')
    for row in reader:

        pgcursor.execute(
                "INSERT INTO energ_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",row)
    pgconnect.commit()
    print('Data insert')
            
    pgcursor.close()
    pgconnect.close()


finally:
    file.close()

print('Fin sans erreurs')