import csv
import sys
import math

def convertToFloat(val):
    try: 
        return float(val)
    except: 
        return val

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




gameList.sort(key=lambda x:x.date) # sort games by date


TeamRatings = {}
defaultRating = None


for game in gameList:
    team1 = game.t1Stats
    team2 = game.t2Stats
    if team1['team'] not in TeamRatings:
        TeamRatings[team1['team']] = defaultRating
    if team2['team'] not in TeamRatings:
        TeamRatings[team2['team']] = defaultRating
    
