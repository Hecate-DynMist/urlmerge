
# coding: utf-8

import pandas as pd
cat = pd.read_excel('techcat.xlsx')
uuid = pd.read_csv('uuid.csv')

def merge(dfc,dfu):
    df = pd.merge(dfc,dfu,right_on='n.name',left_on='Terminology',how='left')
    df['n.name'] = df['n.name'].fillna('另外')
    df.drop(['ID','Category_old'],1,inplace=True)
    df.to_csv('uuidmerge.xlsx',index=False)

merge(cat,uuid)

