import csv
import sys

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
    def __init__(self, t1Stats, t2Stats, id):
        self.t1Stats = t1Stats
        self.t2Stats = t2Stats

gameList = []

for i in range(0,len(dataList), 2):
    gameList.append(Game(dataList[i], dataList[i+1], dataList[i]['game_id']))


print(f'{sys.getsizeof(gameList)} bytes')
