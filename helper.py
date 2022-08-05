# def help_me(): 
#     print("this is a helper function")



# def turnByTurnGrowth(wt_number):
#     '''wt number and returns 
#     a list of the new pop, EC, AC and WC amounts for that tile '''
    
#     popG = wt_number[0]+wt_number[1]
#     ECs = wt_number[2]+wt_number[5]
#     ACs = wt_number[3]+wt_number[6]
#     WCs = wt_number[4]+wt_number[7]
#     return [popG, wt_number[1], ECs, ACs, WCs, wt_number[5],wt_number[6],wt_number[7]]

# def boardTurn(L):
#     '''takes the current worldTile state and returns the state of the board for the next turn'''
#     L0 = []
#     for i in range(len(L)):
#         L0 += [turnByTurnGrowth(L[i])]
#     return L0

# allBuildingsList = ["Village", "Town", "City", "Fortress", "Citadel", "Palace", "Temple", "Lighthouse", "Watchtower", "Wall", "Training Ground", "Smithy"]
# buildingStats = ["Name", "Cost (Population)", "Cost (Earth Cores)", "Cost (Air Cores)", "Cost (Water Cores)"]

# brokefastMountains = {"Name": "The Brokefast Mountains", "Population" : 10, "Pop Growth" : 2, "Earth Growth" : 2, "Air Growth" : 1, "Water Growth" : 0, "Buildings": brokefastMountainsBuildings, "Available Building Slots": 4}
# wanderingForest1 = {"Name": "The Northern Wandering Forest","Population" : 10, "Pop Growth" : 3, "Earth Growth" : 2, "Air Growth" : 0, "Water Growth" : 1, "Buildings": wanderingForest1Buildings, "Available Building Slots": 4}
# easternHighlands = {"Name": "The Eastern Highlands", "Population" : 10, "Pop Growth" : 1, "Earth Growth" : 1, "Air Growth" : 2, "Water Growth" : 0, "Buildings": easternHighlandsBuildings, "Available Building Slots": 4}
# theCitadel = {"Name": "The Citadel", "Population" : 10, "Pop Growth" : 4, "Earth Growth" : 1, "Air Growth" : 1, "Water Growth" : 1, "Buildings": theCitadelBuildings, "Available Building Slots": 4}
# wanderingForest2 = {"Name": "The Southern Wandering Forest", "Population" : 10, "Pop Growth" : 3, "Earth Growth" : 1, "Air Growth" : 0, "Water Growth" : 2, "Buildings": wanderingForest2Buildings, "Available Building Slots": 4}
# easternLowlands = {"Name": "The Eastern Lowlands", "Population" : 10, "Pop Growth" : 1, "Earth Growth" : 0, "Air Growth" : 2, "Water Growth" : 1, "Buildings": easternLowlandsBuildings, "Available Building Slots": 4}
# theFoglands = {"Name": "The Foglands", "Population" : 10, "Pop Growth" : 2, "Earth Growth" : 0, "Air Growth" : 1, "Water Growth" : 2, "Buildings": theFoglandsBuildings, "Available Building Slots": 4}

# allBuildings = [
# village = "Name": "Village", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# town = {"Name": "Town", "Cost: (Village)": 1, "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# city = {"Name": "City", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# fortress = {"Name": "Fortress", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# theCitadel = {"Name": "The Citadel", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# palace = {"Name": "Palace", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# temple = {"Name": "Temple", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# lighthouse = {"Name": "Lighthouse", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# watchtower = {"Name": "Watchtower", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# wall = {"Name": "Wall", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# trainingGrounds = {"Training Grounds": "Village", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}
# smithy = {"Name": "Smity", "Cost (Population)": 100, "Cost (Earth Cores)": 0, "Cost (Air Cores)": 0, "Cost (Water Cores)": 0}]





def count(L, any):
    value = 0
    if len(L) == 0:
        return value
    elif len(L) == 1:
        if L[0] == any:
            return value +1
    else:
        if L[0] == any:
            value += 1
            return count(L[1:], any)
        else:
            return count(L[1:], any)

L = [1, 1, 1, 0]
any = 1

def lookFor(L, any):
    if any in L:
        return True
    else:
        return False

def remOne(L):
    pass


def main(): 
    print(lookFor(L, 2))

    




# World = {"1": brokefastMountains, "2": wanderingForest1, "3": easternHighlands, "4": theCitadel, "5": wanderingForest2, "6": easternLowlands, "7": theFoglands}


# def buildingFunction(allBuildings,buildingStats):
#     newDict = {}

#     num = 1
#     for i in allBuildings:
#         i = {}
#         newDict.update({"building" + str(num): type(i)})


#     print(dict)



    

if __name__ == "__main__": 
    main()
