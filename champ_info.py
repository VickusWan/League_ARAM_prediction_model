# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:13:53 2020

@author: Victor
"""

import json

def champ_info():

    with open(r"C:\Users\Victor\.spyder-py3\champion.json", encoding="utf8") as f:
        data = json.load(f)
        
    f.close()
    
    d = data['data']
    champs = {}
    
    for i in d.values():
        champs[i['key']] = i['id'], i['tags']
        
    return champs

def NameOfChamp(x):
    champ_dic = champ_info()
    x = str(x)
    name = champ_dic[x][0]
    return name
    
def ClassOfChamp(x):
    champ_dic = champ_info()
    x = str(x)
    tags = champ_dic[x][1]
    return tags



# =============================================================================
#         champs['champ'].append(i['id'])
#         champs['id'].append(i['key'])
#         champs['tags1'].append(i['tags'][0])
#         try:
#             champs['tags2'].append(i['tags'][1])
#         except:
#             champs['tags2'].append('N/A')
#             
#     return champs
# 
# =============================================================================

