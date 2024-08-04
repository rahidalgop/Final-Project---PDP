# Libraries
# ===================================================================================================================

import vehicleCollision
import adminFunctions
import generalFunctions
from globalVariables import *
from datetime import datetime
from getpass import getpass

# Functions
# ===================================================================================================================

# Function that displays the menu for judge profile

def menuJudge():

    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MAIN MENU - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Show list of events with status to be approved.")
        print(f"2. Include registration number.")
        print(f"3. Close session.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        while True:
            try:
                option = int(input("Introduce a number: "))
                if option == 1 or option == 2 or option == 3:
                    break
                else:
                    print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")
            except ValueError:
                print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            generalFunctions.closeSession()
            break


