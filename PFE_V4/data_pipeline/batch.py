#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:31:04 2018

@author: Amelie Motteau

"""
from param import to_clean_energ, to_clean_meteo, pgcursor, pgconnect
from function import clean_weather_data, clean_energ_data, create_table, close, insert_data

#-----------------------------BATCH-----------------------------#
clean_weather_data(to_clean_meteo)

clean_energ_data(to_clean_energ)

create_table(pgcursor, pgconnect)

insert_data(pgcursor, pgconnect)
close(pgconnect, pgcursor)

#-----------------------------BATCH-----------------------------#