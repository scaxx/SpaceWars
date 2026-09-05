import json
import datetime

def loadUsers():

    with open("users.json") as users:

        usersDict = json.load(users)

    return usersDict

def saveUsers(usersDict):

    with open("users.json", "w") as users:

        json.dump(usersDict, users)

def userExists(username, users):

    return username in users

def createUser(username, users):
        
    users[username] = ({
        "totalCoins" : 0,
        "unlockedSkins" : ["default"],
        "equippedSkin": "default",
        "scores": []
    })

def updateUserStats(username, users, coins, time, points):

    users[username]["totalCoins"] += coins

    newGame = {
        "date": str(datetime.date.today()),
        "time": time,
        "points": points
    }

    users[username]["scores"].append(newGame)

def rankingSort(users):

    activeUsers = []

    for username, data in users.items():

        #La lista de partidas no está vacía
        if data["scores"]:

            bestGame = max(data["scores"], key = lambda game: game["points"])

            activeUsers.append({
                "username": username, 
                "score": bestGame["points"],
                "time": round(bestGame["time"], 2),
                "date": bestGame["date"]
            })

    sortedR = sorted (

        activeUsers, key = lambda x: x["score"], reverse = True

    )

    return sortedR[:10]