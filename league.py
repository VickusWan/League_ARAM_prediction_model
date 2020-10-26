# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:12:26 2020

@author: Victor
"""

import requests
import champ_info

name = "/lol/summoner/v4/summoners/by-name/"
account = "/lol/match/v4/matchlists/by-account/"
game = "/lol/match/v4/matches/"
spec = [name, account, game]
summoner = "vickus2"


def fetch(typename, body):
    init = "https://na1.api.riotgames.com"
    url = init+typename+body
    payload = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8,la;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": "RGAPI-fb143664-2cd3-4437-af19-3f4d487410ea"
        }
    re = requests.get(url,headers = payload)
    return re.json()


x= fetch(spec[0], summoner)
accountID = x['accountId'] 


x = fetch(spec[1], accountID)
 
m = x['matches']
matches = []

for i in m:
    g = i['gameId']
    g = str(g)
    matches.append(g)
    

x = fetch(spec[2], matches[0])

part = x['participants']

for i in part:
    name = champ_info.NameOfChamp(i['championId'])
    print(name)
    #print(i['championId'],i['stats']['kills'], i['stats']['deaths'], i['stats']['assists'], i['stats']['totalDamageDealt'], i['stats']['timeCCingOthers'], i['stats']['goldEarned'], i['stats']['firstBloodKill'])