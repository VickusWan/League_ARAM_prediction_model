# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:12:26 2020

@author: Victor
"""

import league_data
import pandas as pd

name = "/lol/summoner/v4/summoners/by-name/"
account = "/lol/match/v4/matchlists/by-account/"
game = "/lol/match/v4/matches/"
spec = [name, account, game]
summoner = "vickus2"

x= league_data.fetch(spec[0], summoner)
accountID = x['accountId'] 


x = league_data.fetch(spec[1], accountID)
 
m = x['matches']
matches = []

for i in m:
    g = i['gameId']
    g = str(g)
    matches.append(g)
    

x = league_data.fetch(spec[2], matches[0])

w, l = league_data.match_info(x)
w.pop(0)
l.pop(0)

df = pd.DataFrame(columns=['total kills', 'total deaths', 'total assists', 'Damage Dealt', "Damage Taken", "Time CC'ed", 'Total Gold Earned', 'First Blood Turret', '#Assassins', '#Fighters', "#Mages", "#Marksman", "#Supports", "#Tanks"])

df.loc[0] = w
df.loc[1] = l