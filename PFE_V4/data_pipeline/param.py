#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:59:44 2018

@author: iteis
"""
import psycopg2

pgconnect=psycopg2.connect(dbname='bdd_batch_v4', host='localhost', port='5432', user='postgres', password='1234')

pgcursor=pgconnect.cursor()


to_clean_energ=open('/home/iteis/Documents/PFE_V4/data_pipeline/energ_files/data_energ.csv')

to_clean_meteo = open('/home/iteis/Documents/PFE_V4/data_pipeline/meteo_files/data_meto.csv')
