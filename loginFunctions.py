
# Libraries
# ========================================================================================
import vehicleCollision
from globalVariables import *
from datetime import datetime

# Function that displays the login menu

def displayLoginMenu ():
    while True:
        print("\n")
        print("========================================================")
        print("VEHICLE COLLISION MANAGEMENT PROGRAM")
        print("========================================================\n")
        print("1. Login.")
        print("2. Exit program.\n")
        print("========================================================\n")
        loginMenuOption = input("Introduce a number: ")

        loginMenuOption = validateOption(loginMenuOption)

        if loginMenuOption == 1:
            validateUser()
        elif loginMenuOption == 2:
            print("See you later!")
            break

# Function that validates that user's input in the menu is correct

def validateOption(option):
    while True:
        try:
            option = int(option)
            if option == 1 or option == 2 or option == 3:
                return option
            else:
                print("Invalid argument.")
                option = input("Introduce a valid number: ")
        except ValueError:
            print("Invalid argument.")
            option = input("Introduce a valid number: ")

# Function that validates user login

def validateUser():
    global users, currentUser
    while True:
        idIdentified = False
        id = input("Enter your ID: ")

        for i in range(0, len(users)):
            if users[i]["id"] == id:
                print("\nID was identified.\n")
                idIdentified = True
                userPassword = input("Introduce the password: ")
                if users[i]["password"] == userPassword:
                    print(f"Welcome {users[i]["name"]}.\nYour rol in the system is: {users[i]["profile"]}.")
                    currentUser = id
                    print(f"Current user's ID is {currentUser}.")
                    menuProfile()
                    break
                else:
                    print("Fail, incorrect password.")
                break

        if idIdentified == False:
            print("Fail, ID wasn't identified.")

# Function that displays a menu based on user's profile

def menuProfile():
    global currentUser, users
    for i in range(0, len(users)):
            if users[i]["id"] == currentUser:
                listIndex = i

    if users[listIndex]["profile"] == "administrator":
        menuAdmin()
    elif users[listIndex]["profile"] == "citizen":
        menuCitizen()
    elif users[listIndex]["profile"] == "police":
        menuPolice()
    elif users[listIndex]["profile"] == "judge":
        menuJudge()

# Function that creates a new user

def createNewUser():
    global users
    while True:
        idInUse = False
        newUserID = input("Introduce user's ID: ")
        try:
            newUserID = int(newUserID)
            newUserID = str(newUserID)
            if len(newUserID) != 9:
                print("ID length must be equal to nine. ")
            if len(newUserID) == 9:
                for i in range(0, len(users)):
                    if users[i]["id"] == newUserID:
                        idInUse = True
                if idInUse == True:
                    print("ID is currently assigned to another user. ")
                else:
                    break
        except ValueError:
            print("ID length must be equal to nine and must only contain numerical characters. ")

    newUserName = input("Introduce user's full name: ")
    newUserResidency = input("Introduce user's residency: ")
    newUserAge = input("Introduce user's age: ")
    while True:
        try:
            newUserAge = int(newUserAge)
            break
        except ValueError:
            print("Age must only contain numerical characters.")
            newUserAge = input("Introduce user's age: ")
    while True:
        newUserGender = input("Introduce user's gender (M / F): ")
        if newUserGender.upper() == "M":
            newUserGender = "male"
            break
        elif newUserGender.upper() == "F":
            newUserGender = "female"
            break
        else:
            print("Invalid input.")
    while True:
        format = "%d/%m/%Y"
        newUserBirthdate = input("Introduce user's birthdate (DD/MM/YYYY): ")
        try:
            validFormat = bool(datetime.strptime(newUserBirthdate, format))
            break
        except:
            validFormat = False
            print("Invalid input.")

    while True:
        newUserPassword = input("Introduce user's password: ")
        newUserValidatePassword = input("Confirm user's password: ")
        if newUserPassword == newUserValidatePassword:
            print("New user created correctly. ")
            break
        else:
            print("Passwords do not match. ")

    while True:
        print("Select a profile for the user.")
        print("\n1. Administrator.")
        print("2. Citizen.")
        print("3. Police officer.")
        print("4. Judge.\n")
        profileOption = input("Introduce a number: ")

        try:
            profileOption = int(profileOption)
            if profileOption == 1 or profileOption == 2 or profileOption == 3 or profileOption == 4:
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")

    if profileOption == 1:
        newUserProfile = "administrator"
    elif profileOption == 2:
        newUserProfile = "citizen"
    elif profileOption == 3:
        newUserProfile = "police"
    elif profileOption == 4:
        newUserProfile = "judge"

    newUser = dict()
    newUser["id"] = newUserID
    newUser["name"] = newUserName
    newUser["password"] = newUserPassword
    newUser["age"] = newUserAge
    newUser["gender"] = newUserGender
    newUser["birthdate"] = newUserBirthdate
    newUser["profile"] = newUserProfile
    newUser["residency"] = newUserResidency

    users.append(newUser)
    print("The new user was created successfully.\n")
    for i in users:
        print(i)