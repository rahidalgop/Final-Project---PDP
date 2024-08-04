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
        print(f"{bcolors.OKCYAN}1. Display list of pending approval incidents.")
        print(f"2. Include incident registration number.")
        print(f"3. Close session.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(3)

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            generalFunctions.closeSession()
            break


