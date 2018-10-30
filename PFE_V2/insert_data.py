#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:06:42 2018

@author: iteis
"""
from datetime import datetime
import csv
from param import pgcursor, pgconnect

file2 = open('/home/iteis/Documents/PFE_V2/genereate/csv_meteo2.csv', 'r')
file = open('/home/iteis/Documents/PFE_V2/genereate/csv_meteo.csv', 'r')
file = open('/home/iteis/Documents/PFE_V2/genereate/csv_energ.csv', 'r')


#------------------------------------------------------------------------------#
#try:
#    reader = csv.reader(file2, delimiter=',')
#    next(reader)
#    for row in reader:
#        values = row[1:8]
#        date=datetime.strptime(row[0],'%Y-%m-%d/%H:%M:%S')        
#        values = [date] + values
#        pgcursor.execute(
#                "INSERT INTO sstfr_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",values)
#    pgconnect.commit()
#
#finally:
#    file2.close()
#print('data from csv_meteo2 insert')
#
##------------------------------------------------------------------------------#
#try:
#    reader = csv.reader(file, delimiter=',')
#    next(reader)
#    for row in reader:
#        values = row[1:8]
#        date=datetime.strptime(row[0],'%Y-%m-%d''/''%H:%M:%S')        
#        values = [date] + values
#        pgcursor.execute(
#                "INSERT INTO sstch_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",values)
#    pgconnect.commit()
#finally:
#    file.close()
#print('data from csv_meteo insert')

#------------------------------------------------------------------------------#
try:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        pgcursor.execute(
                "INSERT INTO energ_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",row)
    pgconnect.commit()
finally:
    file.close()
print('data from csv_energ insert')