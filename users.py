import json

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

