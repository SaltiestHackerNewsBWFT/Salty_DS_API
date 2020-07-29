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

for i in range(0, 100000):
    html = urllib.request.urlopen(
        'https://hacker-news.firebaseio.com/v0/item/' + str(i) + '.json')
    data.append(json.loads(html.read()))
    
#%%
data = [i for i in data if i is not None]
#%%
df = pd.DataFrame.from_dict(data)

df_new = df.drop(columns = ['deleted', 'dead', 'descendants', 'score', 'kids', 'parent', 'title', 'url'])
df_new.head(10)
df_commnt = df_new[df_new['type'] == 'comment']
#df_comments.to_sql("HN_comments", con=engine)

#%%
top_100 = ['dang', 'pmiller2', 'throwaway_pdp09', 'dredmorbius', 'smabie',
       'jacquesm', 'supernova87a', 'valuearb', 'catalogia', 'WrtCdEvrydy',
       'amelius', 'baddox', 'perl4ever', 'wolco', 'AnimalMuppet', 'DanBC',
       'thu2111', 'detaro', 'koheripbal', 'dragonwriter', 'nix23',
       'GekkePrutser', 'renewiltord', 'Lammy', 'refurb', 'WalterBright',
       'user5994461', 'mumblemumble', 'scarface74', 'klyrs', 'gruez',
       'ceejayoz', 'dependenttypes', 'Nextgrid', 'gus_massa', 'jariel',
       'pantaloony', 'userbinator', 'Waterfall', 'rumanator',
       'chrisseaton', 'saagarjha', '082349872349872', 'bigiain',
       'auganov', 'thephyber', 'Animats', 'formerly_proven', 'MattGaiser',
       'giantg2', 'Wowfunhappy', 'verdverm', 'ghaff', 'coronadisaster',
       'api', 'm0zg', 'sneak', 'hedora', 'jeffbee', 'hinkley', 'tptacek',
       'thaumasiotes', 'aspenmayer', 'lmm', 'pjmlp', 'fit2rule',
       'AnthonyMouse', 'quickthrower2', 'bananaface', 'eru', 'luckylion',
       'baybal2', 'pjc50', 'mytailorisrich', 'StavrosK', 'imtringued',
       'rsynnott', 'PaulHoule', 'sukilot', 'missedthecue', 'BurningFrog',
       'mensetmanusman', 'Nasrudith', 'nitrogen', 'jessaustin', 'dhosek',
       'totetsu', 'ponker', 'kanobo', 'kerkeslager', 'raxxorrax',
       'throwaway0a5e', 'nabla9', 'duxup', 'vkou', 'DoreenMichele',
       'dencodev', 'shadowgovt', 'robbiejs', 'Shared404', 'proberts']