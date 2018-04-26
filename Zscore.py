#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:34:27 2018

@author: koichirosato
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import pylab as plt
#import numpy as np

font = {'family' : 'IPAexGothic'}
matplotlib.rc('font', **font)
matplotlib.style.use('ggplot')

Location = r'/Users/koichirosato/Documents/data/ZkaiScore.csv'
df = pd.read_csv(Location,index_col='year-month')
df.index = pd.to_datetime(df.index)
df['合計'] = df['国語'].add(df['算数']).add(df['理科'], fill_value=0).add(df['理科'], fill_value=0) 
df['科目数'] = df.loc[:,['国語', '算数', '理科', '社会']].count(axis=1) 
df['平均'] = df['合計']/df['科目数'] 

#colorlist=['#FF0000', '#0000FF', '#008000', '#FFFF00', '#111111']
personlist=['淳生', '莉子']

#rngは、JunとRikoでX軸を揃えたいため、xlimに使用しようと思い作ったが、うまいこと行かない。
#rng = pd.Series(pd.date_range('4/1/2014', periods=46, freq='MS'))

for x in personlist:
    dfx=df[df['person'] == x]
    
    fig, ax = plt.subplots(figsize=(12,3))
    ax.set_title(x)
    ax.set_xlabel('年月')
    ax.set_ylabel('得点')
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax4 = ax.twinx()
    ax5 = ax.twinx()
    ax.bar(dfx.index, dfx['平均'], color='#778899', width=15)
    ax2.plot(dfx.index, dfx['国語'], color='#FF0000', linewidth=2)
    ax3.plot(dfx.index, dfx['算数'], color='#0000FF', linewidth=2)
    ax4.plot(dfx.index, dfx['理科'], color='#008000', linewidth=2)
    ax5.plot(dfx.index, dfx['社会'], color='#FFFF00', linewidth=2)
    ax.set_xlim(pd.Timestamp('2014/3/1'),pd.Timestamp('2018/5/1'))
    ax.set_ylim(0, 105)
    ax2.set_ylim(0, 105)
    ax3.set_ylim(0, 105)
    ax4.set_ylim(0, 105)
    ax5.set_ylim(0, 105)
    ax2.legend(loc='lower left') #複数の凡例を同じ場所に並べて表示する方法は調査中
#    ax = dfx.plot.line(title=x,
#                  y=['国語', '算数', '理科', '社会'],
#                  figsize=(12,3), alpha=10,
#                  grid=True,
#                  color=colorlist, style='.-')
#    ax.set_ylim(0, 105)
#    #rngは、JunとRikoでX軸を揃えたいため、xlimに使用しようと思い作ったが、うまいこと行かない。
#    ax.set_xlim(pd.Timestamp('2014/4/1'),pd.Timestamp('2018/5/1'))
#    #dfx.plot.bar(dfx.index, y=['平均'], position=0.5, ax=ax, color='#778899')
#    plt.show()
