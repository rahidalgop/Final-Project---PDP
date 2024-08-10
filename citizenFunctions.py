
# Libraries
# ===================================================================================================================

import vehicleCollision, adminFunctions, officerFunctions, judgeFunctions, generalFunctions, re
from globalVariables import *
from datetime import datetime, date
from getpass import getpass

# Functions
# ===================================================================================================================

# Function that displays the menu for citizen profile

def menuCitizen():

    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MAIN MENU - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Manage vehicles.")
        print(f"2. Manage events.")
        print(f"3. Close session.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(3)

        if option == 1:
            crudVehicle()
        elif option == 2:
            crudEvent()
        elif option == 3:
            generalFunctions.closeSession()
            break

# Function that executes a CRUD for events / incidents

def crudVehicle():

    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}VEHICLES - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Register new vehicle.")
        print(f"2. Display list of my vehicles.")
        print(f"3. Update vehicle.")
        print(f"4. Delete vehicle.")
        print(f"5. Return to main menu.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(5)

        if option == 1:
            while True:
                validPlateNumber = False
                newVehiclePlate = input("Introduce the vehicle number plate (XXX-000): ")
                
                numberPlateFormat = re.compile('[A-Z]{3}-[0-9]{3}')
                if numberPlateFormat.match(newVehiclePlate) is not None:
                    for i in vehicles:
                        if i["numberPlate"] == newVehiclePlate:
                            print(f"{bcolors.FAIL}\nA vehicle with this plate number is already registered in the system.{bcolors.ENDC}\n")
                            break
                    else:
                        validPlateNumber = True
                else:
                    print(f"{bcolors.FAIL}\nInvalid input.{bcolors.ENDC}\n")
                
                if validPlateNumber == True:
                    break

            while True:
                currentDate = date.today()

                newVehicleYear = input("Introduce the vehicle production year: ")
                try:
                    newVehicleYear = int(newVehicleYear)
                    if newVehicleYear >= 1886 and newVehicleYear <= currentDate.year and newVehicleYear % 1 == 0:
                        break
                    else:
                        print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")
                except ValueError:
                    print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")
            
            print("\nSelect a brand for the vehicle.\n")

            for i in range(0, len(vehicleBrands)):
                print(f"{bcolors.OKCYAN}{i + 1}. {vehicleBrands[i]}.{bcolors.ENDC}")
            print(" ")

            option = generalFunctions.validateOption(10)

            if option == 1:
                newVehicleBrand = "Toyota"
            elif option == 2:
                newVehicleBrand = "Ford"
            elif option == 3:
                newVehicleBrand = "Volkswagen"
            elif option == 4:
                newVehicleBrand = "Nissan"
            elif option == 5:
                newVehicleBrand = "BMW"
            elif option == 6:
                newVehicleBrand = "Chevrolet"
            elif option == 7:
                newVehicleBrand = "Honda"
            elif option == 8:
                newVehicleBrand = "Hyundai"
            elif option == 9:
                newVehicleBrand = "Kia"
            elif option == 10:
                newVehicleBrand = "other"
                
            print("\nSelect a color for the vehicle.\n")

            for i in range(0, len(vehicleColors)):
                print(f"{bcolors.OKCYAN}{i + 1}. {vehicleColors[i].capitalize()}.{bcolors.ENDC}")
            print(" ")

            option = generalFunctions.validateOption(10)

            if option == 1:
                newVehicleColor = "white"
            elif option == 2:
                newVehicleColor = "gray"
            elif option == 3:
                newVehicleColor = "black"
            elif option == 4:
                newVehicleColor = "blue"
            elif option == 5:
                newVehicleColor = "silver"
            elif option == 6:
                newVehicleColor = "red"
            elif option == 7:
                newVehicleColor = "green"
            elif option == 8:
                newVehicleColor = "yellow"
            elif option == 9:
                newVehicleColor = "orange"
            elif option == 10:
                newVehicleColor = "other"

            print("\nSelect a type for the vehicle.")
            print(f"\n{bcolors.OKCYAN}1. Motorcycle.")
            print(f"2. Automobile.")
            print(f"3. Bus.")
            print(f"4. Truck.{bcolors.ENDC}\n")

            option = generalFunctions.validateOption(4)

            if option == 1:
                newVehicleType = "motorcycle"
            elif option == 2:
                newVehicleType = "automobile"
            elif option == 3:
                newVehicleType = "bus"
            elif option == 4:
                newVehicleType = "truck"

            newVehicle = dict()
            newVehicle["ownerID"] = generalFunctions.currentUserID
            newVehicle["numberPlate"] = newVehiclePlate
            newVehicle["year"] = newVehicleYear
            newVehicle["brand"] = newVehicleBrand
            newVehicle["color"] = newVehicleColor
            newVehicle["type"] = newVehicleType

            vehicles.append(newVehicle)
            print(f"\n{bcolors.OKCYAN}New vehicle registered successfully.{bcolors.ENDC}\n")

        elif option == 2:

            print(f"\nThis is the current list of your vehicles.\n")
            print("-----------------------------------------------------------------------------------")
            print(f"{bcolors.BOLD}Vehicles{bcolors.ENDC}")
            print("-----------------------------------------------------------------------------------")
            for i in vehicles:
                if i["ownerID"] == generalFunctions.currentUserID:
                    print(f"Number plate: {i['numberPlate']}, Production year: {i['year']}, Brand: {i['brand']}, Color: {i['color']}, Type: {i['type']}.")
            print("-----------------------------------------------------------------------------------")

        elif option == 3:
            
            printCurrentVehicles()

            while True:
                validPlateNumber = False
                vehicleToModify = input("Introduce the number plate of the vehicle you want to modify: ")

                for i in vehicles:
                    if vehicleToModify == i["numberPlate"] and i["ownerID"] == generalFunctions.currentUserID:
                        validPlateNumber = True
                        vehicleIndex = vehicles.index(i)
                        break
                else:
                    print(f"\n{bcolors.FAIL}A vehicle with this number plate doesn't exist.{bcolors.ENDC}\n")

                if validPlateNumber == True:
                    print("\nSelect a feature to modify.")
                    print(f"\n{bcolors.OKCYAN}1. Number plate.")
                    print(f"2. Production year.")
                    print(f"3. Brand.")
                    print(f"4. Color.")
                    print(f"5. Type.{bcolors.ENDC}\n")

                    modifyOption = generalFunctions.validateOption(5)

                    if modifyOption == 1:
                        while True:
                            validPlateNumber = False
                            newNumberPlate = input("Introduce the vehicle number plate (XXX-000): ")
                            
                            numberPlateFormat = re.compile('[A-Z]{3}-[0-9]{3}')
                            if numberPlateFormat.match(newNumberPlate) is not None:
                                for i in vehicles:
                                    if i["numberPlate"] == newNumberPlate:
                                        print(f"{bcolors.FAIL}\nA vehicle with this plate number is already registered in the system.{bcolors.ENDC}\n")
                                        break
                                else:
                                    validPlateNumber = True
                            else:
                                print(f"{bcolors.FAIL}\nInvalid input.{bcolors.ENDC}\n")
                            
                            if validPlateNumber == True:
                                vehicles[vehicleIndex]["numberPlate"] = newNumberPlate
                                print(f"\n{bcolors.OKCYAN}Vehicle number plate has been updated successfully.{bcolors.ENDC}\n")
                                break

                        break

                    elif modifyOption == 2:
                        while True:
                            currentDate = date.today()

                            newVehicleYear = input("Introduce the new vehicle production year: ")
                            try:
                                newVehicleYear = int(newVehicleYear)
                                if newVehicleYear >= 1886 and newVehicleYear <= currentDate.year and newVehicleYear % 1 == 0:
                                    vehicles[vehicleIndex]["year"] = newVehicleYear
                                    print(f"\n{bcolors.OKCYAN}Vehicle production year has been updated successfully.{bcolors.ENDC}\n")
                                    break
                                else:
                                    print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")
                            except ValueError:
                                print(f"\n{bcolors.FAIL}Please enter a valid number.{bcolors.ENDC}\n")

                        break
                        
                    elif modifyOption == 3:
                        print("\nSelect a new brand for the vehicle.\n")

                        for i in range(0, len(vehicleBrands)):
                            print(f"{bcolors.OKCYAN}{i + 1}. {vehicleBrands[i]}.{bcolors.ENDC}")
                        print(" ")

                        option = generalFunctions.validateOption(10)

                        if option == 1:
                            newVehicleBrand = "Toyota"
                        elif option == 2:
                            newVehicleBrand = "Ford"
                        elif option == 3:
                            newVehicleBrand = "Volkswagen"
                        elif option == 4:
                            newVehicleBrand = "Nissan"
                        elif option == 5:
                            newVehicleBrand = "BMW"
                        elif option == 6:
                            newVehicleBrand = "Chevrolet"
                        elif option == 7:
                            newVehicleBrand = "Honda"
                        elif option == 8:
                            newVehicleBrand = "Hyundai"
                        elif option == 9:
                            newVehicleBrand = "Kia"
                        elif option == 10:
                            newVehicleBrand = "other"

                        vehicles[vehicleIndex]["brand"] = newVehicleBrand
                        print(f"\n{bcolors.OKCYAN}Vehicle brand has been updated successfully.{bcolors.ENDC}\n")

                        break

                    elif modifyOption == 4:
                        print("\nSelect a new color for the vehicle.\n")

                        for i in range(0, len(vehicleColors)):
                            print(f"{bcolors.OKCYAN}{i + 1}. {vehicleColors[i].capitalize()}.{bcolors.ENDC}")
                        print(" ")

                        option = generalFunctions.validateOption(10)

                        if option == 1:
                            newVehicleColor = "white"
                        elif option == 2:
                            newVehicleColor = "gray"
                        elif option == 3:
                            newVehicleColor = "black"
                        elif option == 4:
                            newVehicleColor = "blue"
                        elif option == 5:
                            newVehicleColor = "silver"
                        elif option == 6:
                            newVehicleColor = "red"
                        elif option == 7:
                            newVehicleColor = "green"
                        elif option == 8:
                            newVehicleColor = "yellow"
                        elif option == 9:
                            newVehicleColor = "orange"
                        elif option == 10:
                            newVehicleColor = "other"
                        
                        vehicles[vehicleIndex]["color"] = newVehicleColor
                        print(f"\n{bcolors.OKCYAN}Vehicle color has been updated successfully.{bcolors.ENDC}\n")

                        break
                    
                    elif modifyOption == 5:
                        print("\nSelect a type for the vehicle.")
                        print(f"\n{bcolors.OKCYAN}1. Motorcycle.")
                        print(f"2. Automobile.")
                        print(f"3. Bus.")
                        print(f"4. Truck.{bcolors.ENDC}\n")

                        option = generalFunctions.validateOption(4)

                        if option == 1:
                            newVehicleType = "motorcycle"
                        elif option == 2:
                            newVehicleType = "automobile"
                        elif option == 3:
                            newVehicleType = "bus"
                        elif option == 4:
                            newVehicleType = "truck"

                        vehicles[vehicleIndex]["type"] = newVehicleType
                        print(f"\n{bcolors.OKCYAN}Vehicle type has been updated successfully.{bcolors.ENDC}\n")

                        break

        elif option == 4:

            printCurrentVehicles()

            while True:
                validPlateNumber = False
                vehicleToDelete = input("Introduce the number plate of the vehicle you want to delete: ")

                for i in vehicles:
                    if vehicleToDelete == i["numberPlate"] and i["ownerID"] == generalFunctions.currentUserID:
                        validPlateNumber = True
                        vehicleIndex = vehicles.index(i)
                        break
                else:
                    print(f"\n{bcolors.FAIL}A vehicle with this number plate doesn't exist.{bcolors.ENDC}\n")

                if validPlateNumber == True:
                    del vehicles[vehicleIndex]
                    print(f"\n{bcolors.OKCYAN}Vehicle deleted successfully.{bcolors.ENDC}\n")
                    break
            
        elif option == 5:
            break

# Function that executes a CRUD for events / incidents

def crudEvent():
    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}EVENTS - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Create new event.")
        print(f"2. Display of my events.")
        print(f"3. Update event.")
        print(f"4. Delete event.")
        print(f"5. Return to main menu.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(5)

        if option == 1:
            global events

            pass



        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            break

# Function that prints the current list of user's vehicles

def printCurrentVehicles():

    global vehicles

    print(f"\nThis is the current list of your vehicles' number plate.\n")
    for i in vehicles:
        if i["ownerID"] == generalFunctions.currentUserID:
            print(f"{bcolors.OKCYAN}{i['numberPlate']}{bcolors.ENDC}")
    print("")
