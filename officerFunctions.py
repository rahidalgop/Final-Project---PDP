# Libraries
# ===================================================================================================================

import vehicleCollision, random
from datetime import datetime, timedelta
import adminFunctions
import generalFunctions
from globalVariables import *
from datetime import datetime
from getpass import getpass

# Functions
# ===================================================================================================================

# Function that displays the menu for police officer profile

def menuOfficer():

    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MAIN MENU - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Display list of open events.")
        print(f"2. Include penalty fee number.")
        print(f"3. Close session.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(3)

        if option == 1:
            displayOpenEvents()
        elif option == 2:
            includePenaltyFeeNumber()
        elif option == 3:
            generalFunctions.closeSession()
            break

# Function that displays the list of open events

def displayOpenEvents():

    global events, users, vehicles

    print(f"\nThis is the current list of open events.\n")
    print("-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Open events{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")
    for i in events:
        if i.status == "open" and (datetime.strptime(datetime.now().isoformat(' ', 'seconds'), "%Y-%m-%d %H:%M:%S") - i.dateTime) >= timedelta(seconds = 30):
            print(i.formatIfOpen())
    print("-----------------------------------------------------------------------------------")

# Function that allows the user to include a penalty fee number

def includePenaltyFeeNumber():

    global events, users, vehicles

    print(f"\nThis is the current list of open events.\n")

    for i in events:
        if i.status == "open" and (datetime.strptime(datetime.now().isoformat(' ', 'seconds'), "%Y-%m-%d %H:%M:%S") - i.dateTime) >= timedelta(seconds = 30):
            print(f"{bcolors.OKCYAN}{i.formatIfOpen()}{bcolors.ENDC}")
    print("")

    while True:

        ableToAddFeeNumber = False
        validInput = True

        try:
            eventToAddFeeNumber = input("Introduce the code number of the event you want to include a penalty fee number: ")
            eventToAddFeeNumber = int(eventToAddFeeNumber)

            for x in events:
                if x.code == eventToAddFeeNumber and x.status == "open":
                    ableToAddFeeNumber = True
                    eventIndex = events.index(x)

        except ValueError:
            validInput = False
            print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")

        if ableToAddFeeNumber == False and validInput == True:
            print(f"\n{bcolors.FAIL}An open event with this code number doesn't exist.{bcolors.ENDC}\n")
        elif ableToAddFeeNumber == True and validInput == True:

            while True:
                repeatedNumber = True
                feeNumber = random.randint(100, 999)

                for i in events:
                    if i.penaltyFeeNumber == feeNumber:
                        repeatedNumber = True
                else:
                    repeatedNumber = False

                if repeatedNumber == False:
                    break

            events[eventIndex].penaltyFeeNumber = feeNumber
            events[eventIndex].officerName = generalFunctions.currentUserName
            events[eventIndex].status = "pending approval"
            events[eventIndex].dateTime = datetime.strptime(datetime.now().isoformat(' ', 'seconds'), "%Y-%m-%d %H:%M:%S")
        
            print(f"\n{bcolors.OKCYAN}The penalty fee number {feeNumber} has been added to the event identified with the code {events[eventIndex].code}.\nAdditionally, event status has been set to 'Pending approval' and date-time has been updated.{bcolors.ENDC}\n")

            break







