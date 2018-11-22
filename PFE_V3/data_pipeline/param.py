#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:59:44 2018

@author: iteis
"""
import psycopg2

pgconnect=psycopg2.connect(dbname='bdd_batch_v2', host='localhost', port='5432', user='postgres', password='1234')

pgcursor=pgconnect.cursor()


to_clean_sst=open('/home/iteis/Documents/PFE_V3/data_pipeline/temp_var/rapport_ruc_stch.txt')
to_clean_sst2=open('/home/iteis/Documents/PFE_V3/data_pipeline/temp_var/rapport_ruc_stfr.txt')

to_clean_meteo = open('/home/iteis/Documents/PFE_V3/data_pipeline/temp_var/rapport_uti_met.txt')
