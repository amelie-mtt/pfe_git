#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:25:17 2018

@author: Amelie.MOTTEAU
"""

import pandas as pd 
import glob
import os
#import numpy as np 

try:
    os.chdir('/home/iteis/Documents/PFE_V3/data_pipeline/energ_files')
    allFiles = glob.glob("*")
    dflist=[]
    colonnename=["DATE","ENER_RUC_FRST5,16","ENER_RUC_FRST6,16","ENER_RUC_FRST7,16","ENER_RUC_FRST8,16","ENER_RUC_CHST5,16","ENER_RUC_CHST6,16","ENER_RUC_CHST7,16","ENER_RUC_CHST8,16","ENER_RUC_REF,16"]
    
    for filename in allFiles:
        df = pd.read_csv(filename, header=None, sep=";", skiprows=1)
        dflist.append(df)
        
    
    concatdf=pd.concat(dflist,axis=0)
    concatdf.columns=colonnename
    concatdf.to_csv('/home/iteis/Documents/PFE_V3/data_pipeline/genereate/csv_energ.csv', index=None)

finally:
    print('DONE')