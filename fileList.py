#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: shift_jis
"""
Created on Wed Feb 28 11:54:29 2018

@author: koichirosato
"""

import os
from os.path import join, getsize
import pandas as pd
from math import pi, sqrt

def findAllFiles(directory):
    for root, dirs, files in os.walk(directory):
#                (root.find('自治会') > -1 or root.find('自主防災') > -1) and \
#                root.find('自主防災') > -1  and \
            for file in files:
                if not file.startswith('.') and \
                getsize(join(root, file)) > 0:
                    yield (root + ":" + file +
                          ":" + str(getsize(join(root, file))) +
                          ":" + os.path.splitext(file)[1])

df = pd.DataFrame(index=[], columns=['root', 'file', 'size', 'extension'])

#f = open('fileList_自主防災会資料_jpgresize.txt', 'w')

for file in findAllFiles("/Users/koichirosato/Dropbox/自治会資料"):
#    f.write(file + '\n')

    s = pd.Series(file.split(':'), index=df.columns)
    df = df.append(s, ignore_index=True)

df['size']=df['size'].astype('int')
df_gb = df.groupby('extension')['size'].sum()
df_gb = df_gb.sort_values()
#面積/πの平方根＝半径を利用して、円グラフのサイズを計算
fs = round(sqrt(df_gb.sum() / pi)/3500, 1)
df_gb.plot.pie(figsize=(fs,fs))
print(df_gb.sum())
#f.close()