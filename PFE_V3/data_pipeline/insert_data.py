#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:06:42 2018

@author: iteis
"""
from datetime import datetime
import csv
from param import pgcursor, pgconnect

file2 = open('/home/iteis/Documents/PFE_V3/data_pipeline/genereate/csv_sstfr.csv', 'r')
file = open('/home/iteis/Documents/PFE_V3/data_pipeline/genereate/csv_sstch.csv', 'r')
file_en = open('/home/iteis/Documents/PFE_V3/data_pipeline/genereate/csv_energ.csv', 'r')
file_met = open('/home/iteis/Documents/PFE_V3/data_pipeline/genereate/csv_meteo.csv', 'r')


#------------------------------------------------------------------------------#
try:
    reader = csv.reader(file2, delimiter=',')
    next(reader)
    for row in reader:
        values = row[1:8]
        date=datetime.strptime(row[0],'%y-%m-%d/%H:%M:%S')        
        values = [date] + values
        pgcursor.execute(
                "INSERT INTO sstfr_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",values)
    pgconnect.commit()

finally:
    file2.close()
print('data from csv_sstfr insert')

##------------------------------------------------------------------------------#
try:
    reader2 = csv.reader(file, delimiter=',')
    next(reader2)
    for row in reader2:
        values = row[1:8]
        date=datetime.strptime(row[0],'%y-%m-%d/%H:%M:%S')        
        values = [date] + values
        pgcursor.execute(
                "INSERT INTO sstch_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",values)
    pgconnect.commit()
finally:
    file.close()
print('data from csv_sstch insert')

##------------------------------------------------------------------------------#
#try:
#    reader_m = csv.reader(file_met, delimiter=',')
#    next(reader_m)
#    for row in reader_m:
#        values = row[1:6]
#        date=datetime.strptime(row[0],'%y-%m-%d/%H:%M:%S')        
#        values = [date] + values
#        pgcursor.execute(
#                "INSERT INTO meteo_table VALUES (%s, %s, %s, %s, %s, %s);",values)
#    pgconnect.commit()
#finally:
#    file.close()
#print('data from csv_meteo insert')
#
#------------------------------------------------------------------------------#
try:
    reader3 = csv.reader(file_en)
    next(reader3)
    for row in reader3:
        values = row[1:10]
        date=datetime.strptime(row[0],'%y%m%d%H%M%S%f')        
        values = [date] + values
#17/05/16/23/00/00/448
        pgcursor.execute(
                "INSERT INTO energ_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",values)
    pgconnect.commit()
finally:
    file.close()
print('data from csv_energ insert')