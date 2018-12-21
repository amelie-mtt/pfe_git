#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:04:57 2018

@author: Amelie Motteau
"""

#import pandas as pd
import psycopg2
import pandas as pd

dflist = []

pgconnect=psycopg2.connect(dbname='bdd_batch_v4', host='localhost', port='5432', user='postgres', password='1234')

pgcursor=pgconnect.cursor()

pgcursor.execute("""SELECT * 
FROM energ_table 
INNER JOIN meteo_table
ON energ_table.energ_date = meteo_table.meteo_date""")

aggregate_data = pgcursor.fetchall()

df = pd.DataFrame(data=aggregate_data)
print(df)
titre = ['DATE_ENERG ',
    'ENER_SS_FR_1' ,
    'ENER_SS_FR_2' ,
    'ENER_SS_FR_3' ,
    'ENER_SS_FR_4' ,
    'ENER_SS_CH_1' ,
    'ENER_SS_CH_2' ,
    'ENER_SS_CH_3' ,
    'ENER_SS_CH_4' ,
    'DATE_METEO',
    'TEMPERATURE',
    'PRESSION',
    'ENSOLEILLEMENT',
    'TEMP_HUMIDE',
    'DJU_MOYEN']

df.to_csv('/home/iteis/Documents/PFE_V4/agregate/aggregate_data.csv', header = titre)
