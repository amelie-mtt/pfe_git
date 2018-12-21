#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:06:42 2018

@author: iteis
"""
from datetime import datetime
import csv
from param import pgcursor, pgconnect

file_en = open('/home/iteis/Documents/PFE_V4/data_pipeline/genereate/data_energ.csv', 'r')
file_met = open('/home/iteis/Documents/PFE_V4/data_pipeline/genereate/data_meteo.csv', 'r')


#------------------------------------------------------------------------------#
try:
    reader = csv.reader(file_en, delimiter=',')
    
    for row in reader:
        values = row[1:10]
        pgcursor.execute(
                "INSERT INTO energ_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", values)
    pgconnect.commit()
    print('----------- > ENERG DATA INSERT\n ')


finally:
    file_en.close()

#------------------------------------------------------------------------------#
try:
    reader = csv.reader(file_met, delimiter=',')
    for row in reader:
        values = row[1:7]
        pgcursor.execute(
                "INSERT INTO meteo_table VALUES (%s, %s, %s, %s, %s, %s);",values)
    pgconnect.commit()
    print('----------- > METEO DATA INSERT\n ')


finally:
    file_en.close()


