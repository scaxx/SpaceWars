import json

def loadUsers():

    with open("users.json") as users:
        usersDict = json.load(users)

    return usersDict

def saveUsers(usersDict):
    with open("users.json", "w") as users:
        json.dump(usersDict, users)

