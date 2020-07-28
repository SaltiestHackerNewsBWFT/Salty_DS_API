# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:46:42 2020

@author: Ronin
"""

from sqlalchemy import create_engine

import urllib

import json



import pandas as pd

engine = create_engine(
    "postgres://nidnwrpi:SfFTOS3EQqsV1c4RKQZEtU7O2g8Kic-9@ruby.db.elephantsql.com:5432/nidnwrpi")

data = []

for i in range(0, 10001):
    html = urllib.request.urlopen(
        'https://hacker-news.firebaseio.com/v0/item/' + str(i) + '.json')
    data.append(json.loads(html.read()))
    
#%%
data = [i for i in data if i is not None]
#%%
df = pd.DataFrame.from_dict(data)

df_new = df.drop(columns = ['deleted', 'dead', 'descendants', 'score', 'kids', 'parent', 'title', 'url'])
df_new.head(10)

df_new.to_sql("HN_comments", con=engine)

