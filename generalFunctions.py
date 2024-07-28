
# Libraries
# ========================================================================================
import vehicleCollision
import adminFunctions
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

# Function that validates that user's input in the menu is valid

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

