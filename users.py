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

    if not userExists(username, users):
        
        users[username] = ({
            "total coins" : 0,
            "unlockedSkins" : ["default"],
            "equippedSkins": ["default"],
            "scores": []
        })