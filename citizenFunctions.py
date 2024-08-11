
# Libraries
# ===================================================================================================================

import vehicleCollision, adminFunctions, officerFunctions, judgeFunctions, generalFunctions, re, random, os
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

    global events, vehicles

    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}EVENTS - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Create new event.")
        print(f"2. Display list of my events.")
        print(f"3. Update event.")
        print(f"4. Delete event.")
        print(f"5. Return to main menu.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(5)

        if option == 1:

            printCurrentVehicles()

            while True:
                validPlateNumber = False
                newEventNumberPlate = input("Introduce the number plate of the vehicle involved in the event / incident: ")

                for i in vehicles:
                    if newEventNumberPlate == i["numberPlate"] and i["ownerID"] == generalFunctions.currentUserID and vehicleInEvent(newEventNumberPlate) == False:
                        validPlateNumber = True
                        vehicleIndex = vehicles.index(i)
                        break
                else:
                    print(f"\n{bcolors.FAIL}A vehicle with this number plate doesn't exist or is already vinculated to an event.{bcolors.ENDC}\n")

                if validPlateNumber == True:
                    break

            newEventFine = calculateFine(vehicleIndex)
            print(f"\n{bcolors.OKCYAN}The fine for the selected vehicle will be equal to {newEventFine} colones.{bcolors.ENDC}\n")
            

            while True:
                repeatedCode = True
                newEventCode = random.randint(10000, 99999)

                for i in events:
                    if i.code == newEventCode:
                        repeatedCode = True
                else:
                    repeatedCode = False

                if repeatedCode == False:
                    break
            
            adminFunctions.printCurrentProvinces()
            while True:
                repeatedProvince = False
                provinceName = input("Enter the name of the province in which the event ocurred: ")
                for i in range(0,len(provinces)):
                    if provinceName == provinces[i]["name"]:
                        repeatedProvince = True
                        newEventProvince = provinceName
                        newUserProvinceIndex = i
                        break

                if repeatedProvince == True:
                    break
                else:
                    print(f"\n{bcolors.FAIL}A province with this name doesn't exist.{bcolors.ENDC}\n")
            
            print("\nThis is the current list of cantons within the selected province.\n")
            for i in range(0,len(provinces[newUserProvinceIndex]["cantons"])):
                print(f"{bcolors.OKCYAN}{provinces[newUserProvinceIndex]['cantons'][i]}{bcolors.ENDC}")

            while True:
                repeatedCanton = False
                cantonName = input("\nEnter the name of the canton in which the event ocurred: ")
                for i in range(0,len(provinces[newUserProvinceIndex]["cantons"])):
                    if cantonName == provinces[newUserProvinceIndex]["cantons"][i]:
                        repeatedCanton = True
                        newEventCanton = cantonName
                if repeatedCanton == True:
                    break
                else:
                    print(f"\n{bcolors.FAIL}A canton with this name doesn't exist.{bcolors.ENDC}\n")

            newEventCitizenName = generalFunctions.currentUserName

            newEventDateTime = datetime.now()

            newEvent = Event(newEventCode, newEventCitizenName, (f"{newEventProvince}, {newEventCanton}"), newEventNumberPlate, "Open", newEventDateTime, newEventFine)
            
            events.append(newEvent)

            print(f"\n{bcolors.OKCYAN}New event registered successfully. Code to identify the event: {bcolors.BOLD}{newEventCode}{bcolors.ENDC}{bcolors.ENDC}\n")

        elif option == 2:

            print(f"\nThis is the current list of your events.\n")
            print("-----------------------------------------------------------------------------------")
            print(f"{bcolors.BOLD}Events{bcolors.ENDC}")
            print("-----------------------------------------------------------------------------------")
            currentUserVehicles = []

            for i in vehicles:
                if i["ownerID"] == generalFunctions.currentUserID:
                    currentUserVehicles.append(i)

            for i in currentUserVehicles:
                for x in events:
                    if i["numberPlate"] == x.numberPlate:
                        print(f"Code: {x.code}, Citizen full name: {x.citizenName}, Location: {x.location}, Involved vehicle: {x.numberPlate}, Status: {x.status}, Date-time: {x.dateTime}, Fine: {x.fine}.")
            print("-----------------------------------------------------------------------------------")

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


# Function to determine if a vehicle is currently involved in an event

def vehicleInEvent(numberPlate):

    global vehicles, events

    for i in events:
        if numberPlate == i.numberPlate:
            return True
    else:
        return False
    

# Function to import fines data from txt file and calculate the fine total

def calculateFine(vehicleIndex):
    global vehicles

    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    fines = []
    with open(os.path.join(__location__, "fineTable.txt"), 'r') as f:
        for i in f:
            parameters = i.split(",")
            fine = int(parameters[1]) + (int(parameters[1]) * (int(parameters[2]) / 100))
            fines.append(fine)

    if vehicles[vehicleIndex]["type"] == "motorcycle":
        fine = fines[0]
    elif vehicles[vehicleIndex]["type"] == "automobile":
        fine = fines[1]
    elif vehicles[vehicleIndex]["type"] == "bus":
        fine = fines[2]
    elif vehicles[vehicleIndex]["type"] == "truck":
        fine = fines[3]

    if int(vehicles[vehicleIndex]["year"]) <= 2000:
        fine = fine + (fine * 0.1)

    return fine