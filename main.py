import csv
import sys
import math
# import matplotlib.pyplot as plt


def convertToFloat(val):
    try: 
        return float(val)
    except: 
        return val
    
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

with open("games_2022.csv","r") as f:
    reader = csv.DictReader(f)
    dataList = []
    for row in reader:
        for title in row.keys():
            row[title] = convertToFloat(row[title]) # cleaning up data
        dataList.append(row)
print(f'{sys.getsizeof(dataList)} bytes')
# loaded data into a list of game rows that are labeled now
# for data in dataList:
#     print(data)
# print(len(dataList))

class Game:
    def __init__(self, t1Stats, t2Stats, id, date):
        self.t1Stats = t1Stats
        self.t2Stats = t2Stats
        self.id = id
        self.date = date

gameList = []

for i in range(0,len(dataList), 2):
    gameList.append(Game(dataList[i], dataList[i+1], dataList[i]['game_id'], dataList[i]['game_date']))


def netEfficiency(teamStats, otherteamStats):
    offensive = (teamStats['FGM_2'] + teamStats["FGM_3"] + teamStats["FTM"])/(teamStats['FGA_2'] + teamStats["FGA_3"] + teamStats['FTA'] + teamStats['TOV'])
    defensive= (otherteamStats['FGM_2'] + otherteamStats["FGM_3"] + otherteamStats["FTM"])/(otherteamStats['FGA_2'] + otherteamStats["FGA_3"] + otherteamStats['FTA'] + otherteamStats['TOV'])
    return offensive - defensive

def reboundEfficiency(teamStats, otherteamStats):
    offensiveEff = (teamStats['OREB']/(teamStats['OREB'] + otherteamStats['DREB']))*100
    defensiveEff = (teamStats['DREB']/(teamStats['DREB'] + otherteamStats['OREB']))*100
    return offensiveEff + defensiveEff

def TeamChemistry(teamStats):
    AST = teamStats['AST']
    TOV = teamStats['TOV']
    TOV_TEAM = teamStats['TOV_team']
    return (AST*AST)/(TOV-TOV_TEAM+1)

def TOVPercentage(teamStats):
    return teamStats['TOV']/(teamStats['FGA_2'] + teamStats["FGA_3"] + teamStats['FTA'] + teamStats['TOV'])

def eFGPercentage(teamStats):
    return ((teamStats['FGM_2'] + teamStats["FGM_3"]) + (0.5*teamStats['FGM_3']))/(teamStats['FGA_2']+teamStats['FGA_3'])

def orbPercentage(teamStats, otherteamStats):
    return (teamStats['OREB']/(teamStats['OREB'] + otherteamStats['DREB']))

def ft_FGA(teamStats):
    return teamStats['FTM']/teamStats['FGA']


def skillFactor(teamStats, otherteamStats):
    return eFGPercentage(teamStats) + sigmoid(TeamChemistry(teamStats)) + reboundEfficiency(teamStats, otherteamStats) + 0.5*teamStats['FTM']*(teamStats['FGA'] - teamStats['FGM']) # run ema later


gameList.sort(key=lambda x:x.date) # sort games by date


TeamRatings = {}
defaultRating = 1000


for game in gameList:
    team1 = game.t1Stats
    team2 = game.t2Stats

    if team1['team'] not in TeamRatings:
        TeamRatings[team1['team']] = defaultRating
    if team2['team'] not in TeamRatings:
        TeamRatings[team2['team']] = defaultRating
    ratingDiff = sigmoid(abs(TeamRatings[team1['team']] - TeamRatings[team2['team']]))
    E = 1/(1+math.e**ratingDiff) # add constant K to this 
    margin = abs(team1['team_score'] - team1['opponent_team_score'])
    scoringMargin = 5*math.log(1+margin)/2
    k = 0
    TeamRatings[team1['team']] += ((team1["team_score"] > team1['opponent_team_score']) - E)*((math.log(1+scoringMargin+k)/200)*(20/math.log(200)) + 40)
    TeamRatings[team2['team']] += ((team2["team_score"] > team2['opponent_team_score']) - E)*((math.log(1+scoringMargin+k)/200)*(20/math.log(200)) + 40)
    


top5 = sorted(TeamRatings, key=TeamRatings.get, reverse=True)[:5]
print(top5)
print([TeamRatings[i] for i in top5])