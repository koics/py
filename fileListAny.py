#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:50:03 2018

@author: koichirosato
"""

import os
from os.path import join, getsize

def findAllFiles(directory):
    for root, dirs, files in os.walk(directory):
            for file in files:
                if not file.startswith('.') and \
                getsize(join(root, file)) > 0:
                    yield (root + ":" + file +
                          ":" + str(getsize(join(root, file))) +
                          ":" + os.path.splitext(file)[1])


import pandas as pd

df = pd.DataFrame(index=[], columns=['root', 'file', 'size', 'extension'])

f = open('fileList.txt', 'w')
for file in findAllFiles("/Users/koichirosato/Documents/img/写真"):
    f.write(file + '\n')

    s = pd.Series(file.split(':'), index=df.columns)
    df = df.append(s, ignore_index=True)

df['size']=df['size'].astype('int')
df_gb = df.groupby('extension')['size'].sum()
df_gb = df_gb.sort_values()
fs = round(12 * df_gb.sum() / 500000000, 1)
df_gb.plot.pie(figsize=(fs,fs))

f.close()