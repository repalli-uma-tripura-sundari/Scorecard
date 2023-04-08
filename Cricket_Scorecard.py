import requests
import pandas as pd
import numpy as np


s = 1345038
s = str(s)
m = 1359475
mi = str(m)
r = requests.get(('https://hs-consumer-api.espncricinfo.com/v1/pages/match/scorecard?lang=en&seriesId='+s+'&matchId='+mi),verify = False).json()
##inning_1
#Batting
inning1Bat = r['content']['innings'][0]['inningBatsmen']

le = len(inning1Bat)

inning = []
team = []
name = []
runs = []
out = []
balls = []
fours = []
sixes = []

for i in range(le):
    inn1 = r['match']['teams'][0]['inningNumbers'][0]
    team1 = r['match']['teams'][0]['team']['longName']
    pname = inning1Bat[i]['player']['longName']
    pruns = inning1Bat[i]['runs']
    if inning1Bat[i]['isOut'] == True:
        pout = 0
    else:
        pout = 1
    pballs = inning1Bat[i]['balls']
    pfours = inning1Bat[i]['fours']
    psixes = inning1Bat[i]['sixes']
    
    inning.append(inn1)
    team.append(team1)
    name.append(pname)
    runs.append(pruns)
    out.append(pout)
    balls.append(pballs)
    fours.append(pfours)
    sixes.append(psixes)
    
    
df1 = pd.DataFrame({
    "Inning":inning,
    "Team":team,
    "Name":name,
    "Runs":runs,
    "Out":out,
    "Balls":balls,
    "Fours":fours,
    "Sixes":sixes
})
df1 = df1.fillna(0)
print(df1)
#Bowling
inning1Bowl = r['content']['innings'][0]['inningBowlers']

le = len(inning1Bowl)

inning =[]
team=[]
name=[]
overs=[]
maiden=[]
runs=[]
wickets=[]
noballs=[]
wides=[]

for j in range(le):
    inn1 = r['match']['teams'][0]['inningNumbers'][0]
    team2 = r['match']['teams'][1]['team']['longName']
    pname = inning1Bowl[j]['player']['longName']
    balls = inning1Bowl[j]['balls']
    overcnt = int(balls/6)
    extraballs = int(balls%6)
    if extraballs !=0:
        povers = str(overcnt)+'.'+str(extraballs)
    else:
        povers = overcnt
    pmaiden = inning1Bowl[j]['maidens']
    pruns = inning1Bowl[j]['conceded']
    pwickets = inning1Bowl[j]['wickets']
    pnoballs = inning1Bowl[j]['noballs']
    pwides = inning1Bowl[j]['wides']
    
    inning.append(inn1)
    team.append(team2)
    name.append(pname)
    overs.append(povers)
    maiden.append(pmaiden)
    runs.append(pruns)
    wickets.append(pwickets)
    noballs.append(pnoballs)
    wides.append(pwides)
    
    
df2 = pd.DataFrame({
    "Inning":inning,
    "Team":team,
    "Name":name,
    "Overs":overs,
    "Maiden":maiden,
    "Runs":runs,
    "Wickets":wickets,
    "NoBalls":noballs,
    "Wides":wides
})
df2 = df2.fillna(0)
print(df2)
    
##inning_2
#Batting
inning2Bat = r['content']['innings'][1]['inningBatsmen']

le = len(inning1Bat)

inning = []
team = []
name = []
runs = []
out = []
balls = []
fours = []
sixes = []

for k in range(le):
    inn2 = r['match']['teams'][1]['inningNumbers'][0]
    team1 = r['match']['teams'][1]['team']['longName']
    pname = inning2Bat[k]['player']['longName']
    pruns = inning2Bat[k]['runs']
    if inning2Bat[k]['isOut'] == True:
        pout = 0
    else:
        pout = 1
    pballs = inning2Bat[k]['balls']
    pfours = inning2Bat[k]['fours']
    psixes = inning2Bat[k]['sixes']
    
    inning.append(inn2)
    team.append(team1)
    name.append(pname)
    runs.append(pruns)
    out.append(pout)
    balls.append(pballs)
    fours.append(pfours)
    sixes.append(psixes)
    
    
df3 = pd.DataFrame({
    "Inning":inning,
    "Team":team,
    "Name":name,
    "Runs":runs,
    "Out":out,
    "Balls":balls,
    "Fours":fours,
    "Sixes":sixes
})
df3 = df3.fillna(0)
print(df3)
#Bowling
inning2Bowl = r['content']['innings'][1]['inningBowlers']

le = len(inning2Bowl)

inning =[]
team=[]
name=[]
overs=[]
maiden=[]
runs=[]
wickets=[]
noballs=[]
wides=[]

for l in range(le):
    inn2 = r['match']['teams'][1]['inningNumbers'][0]
    team2 = r['match']['teams'][0]['team']['longName']
    pname = inning2Bowl[l]['player']['longName']
    balls = inning2Bowl[l]['balls']
    overcnt = int(balls/6)
    extraballs = int(balls%6)
    if extraballs !=0:
        povers = str(overcnt)+'.'+str(extraballs)
    else:
        povers = overcnt
    pmaiden = inning2Bowl[l]['maidens']
    pruns = inning2Bowl[l]['conceded']
    pwickets = inning2Bowl[l]['wickets']
    pnoballs = inning2Bowl[l]['noballs']
    pwides = inning2Bowl[l]['wides']
    
    inning.append(inn2)
    team.append(team2)
    name.append(pname)
    overs.append(povers)
    maiden.append(pmaiden)
    runs.append(pruns)
    wickets.append(pwickets)
    noballs.append(pnoballs)
    wides.append(pwides)
    
df4 = pd.DataFrame({
    "Inning":inning,
    "Team":team,
    "Name":name,
    "Overs":overs,
    "Maiden":maiden,
    "Runs":runs,
    "Wickets":wickets,
    "NoBalls":noballs,
    "Wides":wides
    })
df4 = df4.fillna(0)
print(df4)
    
