# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:41:44 2018

@author: Amelie.MOTTEAU
"""

import pandas as pd 
import glob
import os
#import numpy as np 

os.chdir('/home/iteis/Documents/PFE_V1/fichier_netoyer')
allFiles = glob.glob("*")
dflist=[]
colonnename=["DATE","ENER_RUC_FRST5,16","ENER_RUC_FRST6,16","ENER_RUC_FRST7,16","ENER_RUC_FRST8,16","ENER_RUC_CHST5,16","ENER_RUC_CHST6,16","ENER_RUC_CHST7,16","ENER_RUC_CHST8,16","ENER_RUC_REF,16"]
for filename in allFiles:
#    datetimestring = '171001230000789'                                       
#    datetimeobject = datetime.strptime(datetimestring,'%Y%m%d%H%M%S%f')     
#    print(datetimeobject)
    print('ETAPE 1 TA MERE')
    df = pd.read_csv(filename, header=None, sep=";", skiprows=1)
    print(df)
    dflist.append(df)
    

concatdf=pd.concat(dflist,axis=0)
concatdf.columns=colonnename
concatdf.to_csv('/home/iteis/Documents/PFE_V1/genereate/listcomplete.csv', index=None)
print('END')