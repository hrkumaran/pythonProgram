# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:51:08 2020

@author: Dell
"""

from __future__ import print_function

import MySQLdb as my

db = my.connect(host="127.0.0.1",
user="root",
passwd="mysql",
db=""
)

print(db)

cursor = db.cursor()

number_of_rows = cursor.execute("select * from city");

print(number_of_rows)