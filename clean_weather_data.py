#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:01:01 2018

@author: amelie
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:41:44 2018

@author: Amelie.MOTTEAU
"""

import pandas as pd 


df = pd.read_csv('/home/iteis/Documents/PFE_V1/temp_var/rapport_ruc_stch.txt', sep=";")
print('1')

df2 = pd.read_csv('/home/iteis/Documents/PFE_V1/temp_var/rapport_ruc_stfr.txt', sep=";")
print('1,5')

df3 = pd.read_csv('/home/iteis/Documents/PFE_V1/temp_var/rapport_uti_met.txt', sep=";")
print('2')


df.to_csv('/home/iteis/Documents/PFE_V1/genereate/listcompletemeteo.csv', index=None)
df2.to_csv('/home/iteis/Documents/PFE_V1/genereate/listcompletemeteo2.csv', index=None)
df3.to_csv('/home/iteis/Documents/PFE_V1/genereate/listcompletemeteo3.csv', index=None)

print('END')
