


class Player:

    def __init__(self):
        self.playerInfo = {"Type": "Player", "ID": "player", "Name": "", "Earth Cores" : 100, "Air Cores" : 100 , "Water Cores" : 100, "owned_tiles" : {}, "owned_champions": {},}
        # self.stats["Name"] + str(len(worldTileList))
        

    def replacePlayerInfo(self, keyword, newValue):
        if type(keyword) == type(""):
            if type(newValue) == type(self.playerInfo[keyword]):
                self.playerInfo[keyword] += newValue

    def editNumberStats(self, keyword, change):
        if type(keyword) == type(""):
            if type(change) == type(1) or type(''):
                self.playerInfo[keyword] += change

    def addNewStat(self, keyword, newValue):
        if type(keyword) == type(""):      #QUESTION FOR ELLIOT: HOW TO TEST TO MAKE SURE THE KEYWORD IS UNIQUE
            self.playerInfo.update({keyword: newValue})

def createPlayer(L):
    '''takes a list L and returns a dictionary world built from the list with the info attached to tile numbers'''
    newPlayerList = {}
    count = 1
    for i in range(len(L)):
        newPlayer = Player()
        newPlayer.playerInfo["Name"] = L[i]
        newPlayer.playerInfo["ID"] = "player" + str(count)
        label = {newPlayer.playerInfo["Name"]: newPlayer.playerInfo}
        newPlayerList.update(label)

        count +=1
    return newPlayerList
       
def editPlayer(players, name, stat, change):
    '''NUMBERS ONLY'''
    for i in players:
        if type(change) == type(1):
            if name == players[i]["Name"]:
                players[i][stat] += change


playerNames = ["Cory", "Elliot", "Will", "Jack"]
        
playerInfoList={"Type": "Player", "Name": "", "ID": "player", "Earth Cores" : 0, "Air Cores" : 0 , "Water Cores" : 0 ,  "Population Growth": 2}

worldTileList = []
worldTileInfoList = {"Type": "World Tile", "Name": "", "ID": "worldTile", "Population": 10, "Population Growth": 2}





def main():
    print()
    players = createPlayer(playerNames)
    print(players)
    print()
    for i in players:
        print(players[i])
    print()
    players["Cory"]["Earth Cores"] += 2
    editPlayer(players, "Elliot", "Water Cores", -20)
    editPlayer(players, "Will", "Water Cores", 100)

    print()
    for i in players:
        print(players[i])
    


if __name__ == "__main__": 
    main()
