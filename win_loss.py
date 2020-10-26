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
summoner = "Kimchi Poppy Off"
col = ["matchID", 'total kills', 'total deaths', 'total assists', 'Damage Dealt', "Damage Taken", "Time CC'ed", 'Total Gold Earned', 'First Blood Turret', '#Assassins', '#Fighters', "#Mages", "#Marksman", "#Supports", "#Tanks", "WIN/LOSS?"]

x= league_data.fetch(spec[0], summoner)
accountID = x['accountId'] 

dd = pd.read_csv(r"C:\Users\Victor\.spyder-py3\Match_history.csv")

x = league_data.fetch(spec[1], accountID)
 
m = x['matches']
matches = []
count = 0
df = pd.DataFrame(columns=col)

for i in m:
    g = i['gameId']
    g = str(g)
    matches.append(g)
    
for n in matches:

    x = league_data.fetch(spec[2], n)
        
    w, l = league_data.match_info(x)
    
    if len(w) == 0 and len(l) == 0:
        pass
    else:
        w[0] = matches[0]+'W'
        l[0] = matches[0]+'L' 
        w.append('WIN')
        l.append('LOSS')
        
        if w[0] in dd:
            pass
        else:
            df.loc[count] = w
            df.loc[count+1] = l
            count += 2

#df.to_csv(r"C:\Users\Victor\.spyder-py3\Match_history.csv")
#df.to_csv(r"C:\Users\Victor\.spyder-py3\Match_history.csv", mode='a', header=False)