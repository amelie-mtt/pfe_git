#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:04:57 2018

@author: Amelie Motteau
"""

import psycopg2
from param import pgcursor, pgconnect


jsp = pgcursor.execute("SELECT date FROM energ_table UNION SELECT date FROM sstfr_table ORDER BY date")
jsp = pgcursor.fetchall()

print(jsp)

