# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:25:16 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:57:16 2021

@author: User
"""

import pandas as pd
import csv

data1 = pd.read_csv('C:\\work\\Other\\data.csv', sep = ',', header = 1, encoding = 'utf-8-sig', names = ["station_id", "product", "date", "price"])

cat = pd.read_csv('C:\\work\\Other\\catalog_new3.csv', sep = ',', header = 1, encoding = 'utf-8-sig',  names = ["station_id", "Субъект РФ", "Бренд", "№трассы"])

df1 = pd.DataFrame(data = data1)

df2 = pd.DataFrame(data = cat)

df1.price = df1.price.replace('.', ',')

df3=pd.merge(df1, df2, how='left', on = 'station_id')

print(df3)

df3.to_csv(r'C:\\work\\Other\\new_base_short4.csv', encoding = 'utf-8-sig', index = False)