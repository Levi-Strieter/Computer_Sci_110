users = {
    "hannah": "123.pass",
    "alex": "18Flow",
    "wahjudi": "compSci",
    "blake": "budboy12",
}
def acceptLogins(users, username, password):
    if username in users.keys() and password in users.values():
        return True 
    else:
        return False 

loginAccepted = acceptLogins(users, "alex", "18Flow")
print("Login Successful" if loginAccepted else "Login Failed")

def invertDict(dict):
    invertedDict = {y:x for x,y in dict.items()}
    return invertedDict

inverted = invertDict(users)
print(inverted)

student1 = {
    "name": "Wahjudi",
    "homework": [90,89,76,93],
}


