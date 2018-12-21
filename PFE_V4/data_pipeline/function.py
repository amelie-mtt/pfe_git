#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:08:04 2018

@author: iteis
"""

import  pandas as pd
import os 

#-------------------------------------FUNCTION TO CLEAN WETHER DATA--------------------------------#
def clean_weather_data(file):
    df_meteo = pd.read_csv(file, sep=",")
    to_delete_meteo = ['direction','vent_kmh','humide_pourcent','dju_tn','dju_tx','dju_base_16','temperature_test']
    df_meteo = df_meteo.drop(columns=to_delete_meteo)
    df_meteo.to_csv('/home/iteis/Documents/PFE_V4/data_pipeline/genereate/data_meteo.csv', index=None, header = False)
    print('FILE METEO CLEANED')


#-------------------------------------FUNCTION TO CLEAN ENERG DATA FROM SST--------------------------------#
def clean_energ_data(file):
    df_energ = pd.read_csv(file, sep=",")
    to_delete_energ_col = ['CIM_ENER_SS_FR','CIM_ENER_SS_CH','PEV_ENER_SS_FR','PEV_ENER_SS_CH','RUN_ENER_SS_FR_5','RUN_ENER_SS_FR_6','RUN_ENER_SS_FR_7','RUN_ENER_SS_FR_8','RUN_ENER_SS_CH_5','RUN_ENER_SS_CH_6','RUN_ENER_SS_CH_7','AM1_ENER_SS_FR','AM2_ENER_SS_FR','AM1_ENER_SS_CH','AM2_ENER_SS_CH','LOG_ENER_SS_FR','LOG_ENER_SS_CH','GRD_ENER_SS_FR_G','GRD_ENER_SS_FR_I','GRD_ENER_SS_CH_G','GRD_ENER_SS_CH_I','CRP_ENER_SS_FR','CRP_ENER_SS_CH','RES_ENER_SS_FR','RES_ENER_SS_CH','PCE_ENER_SS_CH','UTI_ENER_EG_TCR','UTI_ENER_EC_TCR','RUN_ENER_SS_CH_8']
    df_energ = df_energ.drop(columns=to_delete_energ_col)
    df_energ.to_csv('/home/iteis/Documents/PFE_V4/data_pipeline/genereate/data_energ.csv', index=None, header = False)
    print('FILE ENERG CLEANED')
    

#----------------------------------FUNCTION TO CREATE DATATABLE-------------------------------------#

def create_table(cursor, connect):
    cursor.execute("DROP TABLE IF EXISTS energ_table")
    cursor.execute("""CREATE TABLE energ_table
                     (energ_date date,
                     energ_ruc_sst_fr1 float,
                     energ_ruc_sst_fr2 float,
                     energ_ruc_sst_fr3 float,
                     energ_ruc_sst_fr4 float,
                     energ_ruc_sst_ch1 float,
                     energ_ruc_sst_ch2 float,
                     energ_ruc_sst_ch3 float,
                     energ_ruc_sst_ch4 float);""")
    
    cursor.execute("DROP TABLE IF EXISTS meteo_table")
    cursor.execute("""CREATE TABLE meteo_table
                     (meteo_date date, 
                     temperature float,
                     pression float,
                     ensoleillement float,
                     temp_humide float,
                     dju float);""")

    connect.commit()
    print('DATABASE CREATED')
    
#----------------------------------FUNCTION INSERT DATA INTO DATABASE-------------------------------#
def insert_data(cursor, connect):
    try:
        os.system('python insert_data.py')
        print('INSERTION SUCCED')
        return 0
    except:
        return -1
    print('INSERTION FAIL')
    
#----------------------------------FUNCTION TO CLOSE CONNECTION-------------------------------------#

def close(cursor, connect):
    cursor.close()
    connect.close()
    print('CONNECITON CLOSE')
    
    
