#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:31:04 2018

@author: Amelie Motteau

"""
from param import to_clean_sst, to_clean_sst2, pgcursor, pgconnect, to_clean_meteo
from function import clean_data, clean_energ_data, create_table, close, insert_data, clean_weather_data

#-----------------------------BATCH-----------------------------#
clean_data(to_clean_sst, to_clean_sst2)
clean_weather_data(to_clean_meteo)

clean_energ_data()
create_table(pgcursor, pgconnect)

insert_data(pgcursor, pgconnect)
close(pgconnect, pgcursor)

#-----------------------------BATCH-----------------------------#
