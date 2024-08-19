# Libraries
# ===================================================================================================================

import vehicleCollision, random, os
import adminFunctions
import generalFunctions
from globalVariables import *
from datetime import datetime, timedelta
from getpass import getpass

# Functions
# ===================================================================================================================

# Function that displays the menu for judge profile
'''In this menu, the judge can approve or reject events'''
def menuJudge():

    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MAIN MENU - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Display list of pending approval incidents.")
        print(f"2. Include incident registration number.")
        print(f"3. Close session.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(3)

        if option == 1:
            displayPendingEvents()
        elif option == 2:
            includeIncidentRegistrationNumber()
        elif option == 3:
            generalFunctions.closeSession()
            break


# Function that displays the list of open events and shows the status

def displayPendingEvents():

    global events, users, vehicles

    print(f"\nThis is the current list of pending approval events.\n")
    print("-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Pending approval events{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")
    for i in events:
        if i.status == "pending approval":
            print(i.formatIfPendingApproval())
    print("-----------------------------------------------------------------------------------")

# Function that allows the user to include a penalty fee number
'''Shows the list of pending events and allows the user to include an incident registration number'''
def includeIncidentRegistrationNumber():

    global events, users, vehicles

    anyClosedEvent = False

    for i in events:
        if i.status == "pending approval":
            anyClosedEvent = True

    if anyClosedEvent == True:

        print(f"\nThis is the current list of pending approval events.\n")

        for i in events:
            if i.status == "pending approval":
                print(f"{bcolors.OKCYAN}{i.formatIfPendingApproval()}{bcolors.ENDC}")
        print("")

        while True:

            ableToAddIncidentRegNumber = False
            validInput = True

            try:
                eventToAddincidentRegNumber = input("Introduce the code number of the event you want to include an incident registration number: ")
                eventToAddincidentRegNumber = int(eventToAddincidentRegNumber)

                for x in events:
                    if x.code == eventToAddincidentRegNumber and x.status == "pending approval":
                        ableToAddIncidentRegNumber = True
                        eventIndex = events.index(x)

            except ValueError:
                validInput = False
                print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")

            if ableToAddIncidentRegNumber == False and validInput == True:
                print(f"\n{bcolors.FAIL}A pending approval event with this code number doesn't exist.{bcolors.ENDC}\n")
            elif ableToAddIncidentRegNumber == True and validInput == True:

                while True:
                    repeatedNumber = True
                    incidentRegNumber = random.randint(100, 999)

                    for i in events:
                        if i.registerNumber == incidentRegNumber:
                            repeatedNumber = True
                    else:
                        repeatedNumber = False

                    if repeatedNumber == False:
                        break

                events[eventIndex].registerNumber = incidentRegNumber
                events[eventIndex].judgeName = generalFunctions.currentUserName
                events[eventIndex].status = "closed"
                events[eventIndex].dateTime = datetime.strptime(datetime.now().isoformat(' ', 'seconds'), "%Y-%m-%d %H:%M:%S")
            
                print(f"\n{bcolors.OKCYAN}The incident registration number {incidentRegNumber} has been added to the event identified with the code {events[eventIndex].code}.\nAdditionally, event status has been set to 'Closed' and date-time has been updated.{bcolors.ENDC}\n")

                writeClosedEventsOnFile()

                break

    else:
        print(f"\n{bcolors.FAIL}There are currently no pending approval events.{bcolors.ENDC}\n")


# Function that creates / cleans a txt file and writes all closed events on it
'''Writes all closed events on a txt file with the location of the program'''
def writeClosedEventsOnFile():

    global events, users, closedEvents

    closedEvents = []

    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "closedEvents.txt"), 'w') as f:
        for i in events:
            if i.status == "closed":
                f.write(f"{i.formatToFile()}")
    print(f"\n{bcolors.OKCYAN}Closed events list saved on 'closedEvents.txt' file.{bcolors.ENDC}\n")

