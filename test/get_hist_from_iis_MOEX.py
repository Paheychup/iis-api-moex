# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:49:48 2021

@author: Павел
"""

#import requests, csv
import pandas as pd
import numpy as np
import os

start=0
stop=501 #max rows returned by moex iis using request
code='SiZ1'

dateFrom='2021-12-09'
dateTill='2021-12-09'

print(os.getcwd())
wdir=('d:\\Anaconda3\\My_scripts\\IIS_Moex\\historyIIS\\')
if os.getcwd()!=wdir: os.chdir(wdir)

url = 'https://iss.moex.com/iss/engines/futures/markets/forts/boards/FOB/'\
    'securities/'+code+'/candles.csv?interval=1&from='+dateFrom+'&till='+ dateTill +'&start='


for i in np.arange(start,stop,500):
    url=url+str(i)
    df = pd.read_csv(url,sep=';',header=1)

    try:
        len(df_hist.index)
    except:
        df_hist=df.copy()
      
    if len(df_hist.index)==0:
        df_hist=df.copy()
    elif i!=0:
        df_hist=df_hist.append(df)

if not os.path.exists(''+dateFrom+'_'+code+''): 
            os.makedirs(''+dateFrom+'_'+code+'')
pd.DataFrame.to_csv(df_hist,wdir
                    +dateFrom+'_'+code+'\\'+dateFrom+'_'+code+ '.txt',index=False,sep=';')
        
        
#resample data
df=df_hist.copy()        
df.dtypes
df.begin=pd.to_datetime(df.begin)
df=df.set_index('begin')
data_5Min = df['close'].resample('5Min').ohlc()

'''
df = df.drop(['open','high','low','value','end'], axis=1)
df =df.rename({'begin':'DateTime'}, axis=1)
'''
#reset index
data_5Min.reset_index(drop=False,inplace=True)
data_5Min.dtypes

#convert datetime index to string columns
data_5Min['date']=data_5Min['DateTime'].dt.strftime('%Y%m%d')
data_5Min['time']=data_5Min['DateTime'].dt.strftime('%H%M%S')

data_5Min['DateTime'].astype(str)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
