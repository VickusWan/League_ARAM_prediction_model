# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:37:02 2020

@author: Victor
"""

import champ_info
import requests

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


def match_info(x):
    
    win = []
    loss = []
    for i in x['teams']:
        if i['win'] == 'Win':
            win.append(i['teamId'])
        else:
            loss.append(i['teamId'])
    
    part = x['participants']
    
    kills_win = 0
    deaths_win = 0
    assists_win = 0
    dmg_win = 0
    dmg_taken_win = 0
    CC_win = 0
    gold_win = 0
    firstTurret_win = 0
    assassin_win = 0
    fighter_win = 0
    mage_win = 0
    marksman_win = 0
    support_win = 0
    tank_win = 0
    
    kills_loss = 0
    deaths_loss = 0
    assists_loss = 0
    dmg_loss = 0
    dmg_taken_loss = 0
    CC_loss = 0
    gold_loss = 0
    firstTurret_loss = 0
    assassin_loss = 0
    fighter_loss = 0
    mage_loss = 0
    marksman_loss = 0
    support_loss = 0
    tank_loss = 0
    
    
    for i in part:
        #name = champ_info.NameOfChamp(i['championId'])
        cl = champ_info.ClassOfChamp(i['championId'])

        if i['teamId'] == win[0]:
            
            kills_win += i['stats']['kills']
            deaths_win += i['stats']['deaths']
            assists_win += i['stats']['assists']
            dmg_win += i['stats']['totalDamageDealt']
            dmg_taken_win += i['stats']['totalDamageTaken']
            CC_win += i['stats']['timeCCingOthers']
            gold_win += i['stats']['goldEarned']
            if i['stats']['firstTowerKill'] == False:
                firstTurret_win += 0
            else:
                firstTurret_win += 1
            
            if cl[0] == 'Assassin':
                assassin_win += 1
            elif cl[0] == 'Fighter':
                fighter_win += 1
            elif cl[0] == 'Mage':
                mage_win += 1
            elif cl[0] == 'Marksman':
                marksman_win += 1
            elif cl[0] == 'Support':
                support_win += 1
            elif cl[0] == 'Tank':
                tank_win += 1
                
            try:
                cl[1]
                if cl[1] == 'Assassin':
                    assassin_win += 1
                elif cl[1] == 'Fighter':
                    fighter_win += 1
                elif cl[1] == 'Mage':
                    mage_win += 1
                elif cl[1] == 'Marksman':
                    marksman_win += 1
                elif cl[1] == 'Support':
                    support_win += 1
                elif cl[1] == 'Tank':
                    tank_win += 1
            except:
                pass
     
        else:
            kills_loss += i['stats']['kills']
            deaths_loss += i['stats']['deaths']
            assists_loss += i['stats']['assists']
            dmg_loss += i['stats']['totalDamageDealt']
            dmg_taken_loss += i['stats']['totalDamageTaken']
            CC_loss += i['stats']['timeCCingOthers']
            gold_loss += i['stats']['goldEarned']
            if i['stats']['firstTowerKill'] == False:
                firstTurret_loss += 0
            else:
                firstTurret_loss += 1
    
            if cl[0] == 'Assassin':
                assassin_loss += 1
            elif cl[0] == 'Fighter':
                fighter_loss += 1
            elif cl[0] == 'Mage':
                mage_loss += 1
            elif cl[0] == 'Marksman':
                marksman_loss += 1
            elif cl[0] == 'Support':
                support_loss += 1
            elif cl[0] == 'Tank':
                tank_loss += 1
                
            try:
                cl[1]
                if cl[1] == 'Assassin':
                    assassin_loss += 1
                elif cl[1] == 'Fighter':
                    fighter_loss += 1
                elif cl[1] == 'Mage':
                    mage_loss += 1
                elif cl[1] == 'Marksman':
                    marksman_loss += 1
                elif cl[1] == 'Support':
                    support_loss += 1
                elif cl[1] == 'Tank':
                    tank_loss += 1
            except:
                pass
            
    win.append(kills_win)
    win.append(deaths_win)
    win.append(assists_win)
    win.append(dmg_win)
    win.append(dmg_taken_win)
    win.append(CC_win)
    win.append(gold_win)
    win.append(firstTurret_win)
    win.append(assassin_win)
    win.append(fighter_win)
    win.append(mage_win)
    win.append(marksman_win)
    win.append(support_win)
    win.append(tank_win)
    
    loss.append(kills_loss)
    loss.append(deaths_loss)
    loss.append(assists_loss)
    loss.append(dmg_loss)
    loss.append(dmg_taken_loss)
    loss.append(CC_loss)
    loss.append(gold_loss)
    loss.append(firstTurret_loss)
    loss.append(assassin_loss)
    loss.append(fighter_loss)
    loss.append(mage_loss)
    loss.append(marksman_loss)
    loss.append(support_loss)
    loss.append(tank_loss)
    
    return win, loss