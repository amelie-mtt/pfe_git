#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:08:04 2018

@author: iteis
"""

import  pandas as pd
import os 

#-------------------------------------FUNCTION TO CLEAN WEATHER DATA--------------------------------#
def clean_data(file1, file2):
    df_meteo = pd.read_csv(file1, sep=';')
    df_meteo.to_csv('/home/iteis/Documents/PFE_V2/genereate/csv_meteo.csv', index=None)
    print('file meteo to csv')
    
    df_meteo2 = pd.read_csv(file2, sep=';')
    df_meteo2.to_csv('/home/iteis/Documents/PFE_V2/genereate/csv_meteo2.csv', index=None)
    print('file meteo2 to csv')
    
#------------------------------------FUNCTION TO CLEAN ENERG DATA-----------------------------------#

def clean_energ_data():
    try:
        os.system('python concat_clean_energ_file.py')
        print('file concat')
        return 0
    except:
        return -1
    print('fail concat')

#----------------------------------FUNCTION TO CREATE DATATABLE-------------------------------------#

def create_table(cursor, connect):
    cursor.execute("DROP TABLE IF EXISTS energ_table")
    cursor.execute("""CREATE TABLE energ_table
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
    cursor.execute("DROP TABLE IF EXISTS sstfr_table")
    cursor.execute("""CREATE TABLE sstfr_table
                     (date timestamp, 
                     sst_fr_1 float, 
                     sst_fr_2 float, 
                     sst_fr_3 float, 
                     sst_fr_4 float, 
                     sst_fr_5 float, 
                     sst_fr_6 float, 
                     sst_fr_7 float, 
                     sst_fr_8 float);""")
    cursor.execute("DROP TABLE IF EXISTS sstch_table")
    cursor.execute("""CREATE TABLE sstch_table
                     (date timestamp, 
                     sst_ch_1 float, 
                     sst_ch_2 float, 
                     sst_ch_3 float, 
                     sst_ch_4 float, 
                     sst_ch_5 float, 
                     sst_ch_6 float, 
                     sst_ch_7 float, 
                     sst_ch_8 float);""")
    connect.commit()
    print('database created')
    
#----------------------------------FUNCTION INSERT DATA INTO DATABASE-------------------------------#
def insert_data(cursor, connect):
    try:
        os.system('python insert_data.py')
        print('data inserteds')
        return 0
    except:
        return -1
    print('fail concat')
    
#----------------------------------FUNCTION TO CLOSE CONNECTION-------------------------------------#

def close(cursor, connect):
    cursor.close()
    connect.close()
    print('connection close')
    
    
