
# Libraries
# ===================================================================================================================

import vehicleCollision, adminFunctions, officerFunctions, judgeFunctions, citizenFunctions
from globalVariables import *
from datetime import datetime
from getpass import getpass

# Functions
# ===================================================================================================================
''' IMPORTANT!
The global variable indicate that they're defined outside of each of these functions
(there maybe several) but thar they used within the functions that is relevant to them'''
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
        
        option = validateOption(2)

        if option == 1:
            validateUser()
        elif option == 2:
            print(f"\n{bcolors.OKCYAN}See you later!{bcolors.ENDC}\n")
            break

# Function that validates that user's input in the menu is valid
'''This function makes sure that the data entered by the user is an integer within the 
specified range (optionsQuantity)'''                       

def validateOption(optionsQuantity):
    while True:
        option = input("Introduce a number: ")
        try:
            option = int(option)
            if option >= 1 and option <= optionsQuantity and option % 1 == 0:
                return option
            else:
                print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")
        except ValueError:
            print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")

# Function that validates user login
'''This method used to validate the user consistence in the system using the ID in a list of created data(for i in users),
if it's the case it will ask for the associated password, otherwise it will ask for the ID again and send an error message'''
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
                userPassword = getpass("Introduce your password (hidden while you write): ")
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
'''This menu redirects the user to the correct menu based on the user's profile (taking into account that it's the administrator
who defines the role of the user)'''
def menuProfile():
    global currentUser, users
    for i in range(0, len(users)):
            if users[i]["id"] == currentUser:
                listIndex = i

    if users[listIndex]["profile"] == "administrator":
        adminFunctions.menuAdmin()
    elif users[listIndex]["profile"] == "citizen":
        citizenFunctions.menuCitizen()
    elif users[listIndex]["profile"] == "police officer":
        officerFunctions.menuOfficer()
    elif users[listIndex]["profile"] == "judge":
        judgeFunctions.menuJudge()

# Function that closes current user session

def closeSession():
    global currentUser
    currentUser = False

# Function that creates a variable for current user's name and role
'''With this function we can get the name and role of the current user and update the current user information so that 
it allows us to mobilie anywhere in the code'''
def currentUserInfo(id):
    global currentUser, currentUserName, currentUserProfile, currentUserID
    for i in range(0, len(users)):
        if id == users[i]["id"]:
            currentUserName = users[i]["name"]
            currentUserProfile = users[i]["profile"]
            currentUserID = id

# Function that returns current user's name and role

def printUserInfo():
    global currentUserName, currentUserProfile
    return f"{bcolors.OKCYAN}Logged as {currentUserName} ({currentUserProfile}){bcolors.ENDC}"

