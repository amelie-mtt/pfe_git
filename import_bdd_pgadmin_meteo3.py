#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:38:24 2018

@author: Amelie Motteau
"""
import csv
import psycopg2
from datetime import datetime


pgconnect = psycopg2.connect(dbname='bdd_test', host='localhost', port='5432', user='postgres', password='1234')
print('Connection')

pgcursor=pgconnect.cursor()

pgcursor.execute("DROP TABLE IF EXISTS sstfr_table")
pgcursor.execute("""CREATE TABLE sstfr_table
                 (date timestamp, 
                 sst_fr_1 float, 
                 sst_fr_2 float, 
                 sst_fr_3 float, 
                 sst_fr_4 float, 
                 sst_fr_5 float, 
                 sst_fr_6 float, 
                 sst_fr_7 float, 
                 sst_fr_8 float);""")


print('Creation DB')


file = open('/home/iteis/Documents/PFE_V1/genereate/listcompletemeteo2.csv', 'r')

try:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    
    for row in reader:
        values = row[1:8]
        
        date=datetime.strptime(row[0],'%Y-%m-%d/%H:%M:%S')        
        #AA-MM-JJ/hh:mm:ss
        values = [date] + values
        
        pgcursor.execute(
                "INSERT INTO sstfr_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",values)
    pgconnect.commit()
    print('Data insert')
            
    pgcursor.close()
    pgconnect.close()


finally:
    file.close()

print('Fin sans erreurs')