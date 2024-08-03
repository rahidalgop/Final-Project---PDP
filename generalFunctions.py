
# Libraries
# ===================================================================================================================

import vehicleCollision
import adminFunctions
from globalVariables import *
from datetime import datetime
from getpass import getpass

# Functions
# ===================================================================================================================

# Function that displays the login menu

def loginMenu ():
    global currentUser
    currentUser = 1
    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}VEHICLE COLLISION MANAGEMENT PROGRAM{bcolors.ENDC}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Login.")
        print(f"2. Exit program.\n{bcolors.ENDC}")
        print("===================================================================================\n")
        loginMenuOption = input("Introduce a number: ")

        loginMenuOption = validateOption(loginMenuOption)

        if loginMenuOption == 1:
            validateUser()
        elif loginMenuOption == 2:
            print(f"\n{bcolors.OKCYAN}See you later!{bcolors.ENDC}\n")
            break

# Function that validates that user's input in the menu is valid

def validateOption(option):
    while True:
        try:
            option = int(option)
            if option == 1 or option == 2 or option == 3:
                return option
            else:
                print(f"\n{bcolors.FAIL}Invalid argument.{bcolors.ENDC}\n")
                option = input("Introduce a valid number: ")
        except ValueError:
            print(f"\n{bcolors.FAIL}Invalid argument.{bcolors.ENDC}\n")
            option = input("Introduce a valid number: ")

# Function that validates user login

def validateUser():
    global users, currentUser
    while True:
        if currentUser == False:
            currentUser = 1
            break
        idIdentified = False
        id = input("Enter your ID: ")

        for i in range(0, len(users)):
            if users[i]["id"] == id:
                print(f"\n{bcolors.OKCYAN}ID was correctly identified.{bcolors.ENDC}\n")
                idIdentified = True
                userPassword = getpass("Introduce your password: ")
                if users[i]["password"] == userPassword:
                    print("\n-----------------------------------------------------------------------------------")
                    print(f"{bcolors.OKCYAN}Welcome {users[i]['name']}.\nYour rol in the system is: {users[i]['profile']}.{bcolors.ENDC}")
                    currentUser = id
                    currentUserInfo(id)
                    print("-----------------------------------------------------------------------------------")
                    menuProfile()
                    break
                else:
                    print(f"\n{bcolors.FAIL}Fail, incorrect password.{bcolors.ENDC}\n")
                break

        if idIdentified == False:
            print(f"\n{bcolors.FAIL}Fail, ID wasn't identified.{bcolors.ENDC}\n")

# Function that displays a menu based on user's profile

def menuProfile():
    global currentUser, users
    for i in range(0, len(users)):
            if users[i]["id"] == currentUser:
                listIndex = i

    if users[listIndex]["profile"] == "administrator":
        adminFunctions.menuAdmin()
    elif users[listIndex]["profile"] == "citizen":
        pass
    elif users[listIndex]["profile"] == "police":
        pass
    elif users[listIndex]["profile"] == "judge":
        pass

# Function that closes current user session

def closeSession():
    global currentUser
    currentUser = False

# Function that creates a variable for current user's name and role

def currentUserInfo(id):
    global currentUserName, currentUserProfile
    for i in range(0, len(users)):
        if id == users[i]["id"]:
            currentUserName = users[i]["name"]
            currentUserProfile = users[i]["profile"]

def printUserInfo():
    global currentUserName, currentUserProfile
    return f"{bcolors.OKCYAN}Logged as {currentUserName} ({currentUserProfile}).{bcolors.ENDC}"
