
# Libraries
# ===================================================================================================================

import generalFunctions, os, judgeFunctions
from globalVariables import *
from datetime import datetime
from getpass import getpass

# Functions
# ===================================================================================================================

# Function that displays the menu for admin profile (CRUD)

def menuAdmin():
    global currentUser, users, currentUserProfile, currentUserName
    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MAIN MENU - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Create user.")
        print(f"2. Manage provinces.")
        print(f"3. Manage cantons.")
        print(f"4. Reports.")
        print(f"5. Close session.{bcolors.ENDC}")
        print("\n===================================================================================\n")

        option = generalFunctions.validateOption(5)
#This part of the code calls the function created for this crud
        if option == 1:
            createNewUser()
        elif option == 2:
            crudProvince()
        elif option == 3:
            crudCanton()
        elif option == 4:
            reportsMenu()
        elif option == 5: 
            generalFunctions.closeSession()
            break

# Function that prints the current list of provinces in the system

def printCurrentProvinces():

    global provinces

    print("\nThis is the current list of provinces.\n")
    for i in range(0,len(provinces)):
        print(f"{bcolors.OKCYAN}{provinces[i]['name']}{bcolors.ENDC}")
    print("") 

# Function that prints the current list of cantons in the system

def printCurrentCantons():

    global provinces

    print("\nThis is the current list of cantons.\n")
    for i in range(0,len(provinces)):
        for x in range(0,len(provinces[i]["cantons"])):
            print(f"{bcolors.OKCYAN}{provinces[i]['cantons'][x]}{bcolors.ENDC}")
    print("")

# Function that creates a new user
''' This is the most essential part of the program, since here a 9 digit numerical user is 
created (it cannot be the same as the admin), with it's respective password. who can choose cantons and provinces(stored) 
and is asked for gender and age.Some data come with a specific requirement that if typed differently, an error will appear
until it is correct. And at the end the user is stored in the system list. '''

def createNewUser():
    global users
    while True:
        idInUse = False
        newUserID = input("Introduce user's ID: ")
        try:
            newUserID = int(newUserID)
            newUserID = str(newUserID)
            if len(newUserID) != 9:
                print(f"\n{bcolors.FAIL}ID length must be equal to nine. {bcolors.ENDC}\n")
            if len(newUserID) == 9:
                for i in range(0, len(users)):
                    if users[i]["id"] == newUserID:
                        idInUse = True
                if idInUse == True:
                    print(f"{bcolors.FAIL}\nThe ID is currently assigned to another user. {bcolors.ENDC}\n")
                else:
                    break
        except ValueError:
            print(f"{bcolors.FAIL}\nID length must be equal to nine and must only contain numerical characters. {bcolors.ENDC}\n")

    newUserName = input("Introduce user's full name: ")

    printCurrentProvinces()
    while True:
        repeatedProvince = False
        provinceName = input("Enter the name of the province in which the user lives: ")
        for i in range(0,len(provinces)):
            if provinceName == provinces[i]["name"]:
                repeatedProvince = True
                newUserProvince = provinceName
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
        cantonName = input("\nEnter the name of the canton in which the user lives: ")
        for i in range(0,len(provinces[newUserProvinceIndex]["cantons"])):
            if cantonName == provinces[newUserProvinceIndex]["cantons"][i]:
                repeatedCanton = True
                newUserCanton = cantonName
        if repeatedCanton == True:
            break
        else:
            print(f"\n{bcolors.FAIL}A canton with this name doesn't exist.{bcolors.ENDC}\n")

    newUserAge = input("Introduce user's age: ")
    while True:
        try:
            newUserAge = int(newUserAge)
            if newUserAge >= 18:
                break
            else:
                print(f"{bcolors.FAIL}\nUnderage users are not allowed in the system.{bcolors.ENDC}\n")
                newUserAge = input("Introduce user's age: ")
        except ValueError:
            print(f"{bcolors.FAIL}\nAge must only contain numerical characters.{bcolors.ENDC}\n")
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
            print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")
    while True:
        format = "%d/%m"
        newUserBirthdate = input("Introduce user's birthdate (DD/MM): ")
        try:
            bool(datetime.strptime(newUserBirthdate, format))
            break
        except:
            print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")

    while True:
        newUserPassword = getpass("Introduce user's password (hidden while you write): ")
        newUserValidatePassword = getpass("Confirm user's password (hidden while you write): ")
        if newUserPassword == newUserValidatePassword:
            break
        else:
            print(f"\n{bcolors.FAIL}Passwords do not match.{bcolors.ENDC}\n")

    while True:
        print("\nSelect a profile for the user.")
        print(f"\n{bcolors.OKCYAN}1. Citizen.")
        print(f"2. Police officer.")
        print(f"3. Judge.{bcolors.ENDC}\n")
        profileOption = input("Introduce a number: ")

        try:
            profileOption = int(profileOption)
            if profileOption == 1 or profileOption == 2 or profileOption == 3:
                break
            else:
                print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")
        except ValueError:
            print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")

    if profileOption == 1:
        newUserProfile = "citizen"
    elif profileOption == 2:
        newUserProfile = "police officer"
    elif profileOption == 3:
        newUserProfile = "judge"

    newUser = dict()
    newUser["id"] = newUserID
    newUser["name"] = newUserName
    newUser["password"] = newUserPassword
    newUser["profile"] = newUserProfile
    newUser["gender"] = newUserGender
    newUser["age"] = newUserAge
    newUser["residency"] = f"{newUserProvince}, {newUserCanton}"
    newUser["birthdate"] = newUserBirthdate

    users.append(newUser)
    print(f"\n{bcolors.OKCYAN}New user created successfully.{bcolors.ENDC}\n")

# Function that executes a CRUD for provinces
'''This function allows the administrator to create, display, update and delete provinces'''
def crudProvince():
    global provinces
    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MANAGE PROVINCES - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Create province.")
        print(f"2. Display provinces list.")
        print(f"3. Update province.")
        print(f"4. Delete province.")
        print(f"5. Return to main menu.{bcolors.ENDC}")
        print("\n===================================================================================\n")
        
        option = generalFunctions.validateOption(5)
        ''' Following the menu. Request the name of the new princes(verify that it doesn't exist in the system) 
        and add it to the list of provinces '''
        if option == 1:
            while True:
                repeatedProvince = False
                name = input("Enter province name: ")
                for i in range(0,len(provinces)):
                    if name == provinces[i]["name"]:
                        repeatedProvince = True

                if repeatedProvince == True:
                    print(f"{bcolors.FAIL}\nA province with this name already exists.{bcolors.ENDC}\n")
                else:
                    break
            newProvince = dict()
            newProvince["name"] = name
            newProvince["cantons"] = []
            provinces.append(newProvince)
            print(f"\n{bcolors.OKCYAN}The province was added correctly.\n{bcolors.ENDC}")

            ''' Display the list of provinces '''
        elif option == 2:
            print(f"\nThis is the current list of provinces.\n")
            print("-----------------------------------------------------------------------------------")
            print(f"{bcolors.BOLD}Provinces{bcolors.ENDC}")
            print("-----------------------------------------------------------------------------------")
            for i in range(0,len(provinces)):
                print(provinces[i]["name"])
            print("-----------------------------------------------------------------------------------")
            ''' Update province name (verify that the province exists) '''
        elif option == 3:
            printCurrentProvinces()

            while True:
                repeatedProvince = False
                name = input("Enter the name of the province to update: ")
                for i in provinces:
                    if i["name"] == name:
                        provinceIndex = provinces.index(i)
                        repeatedProvince = True
                if repeatedProvince == False:
                    print(f"\n{bcolors.FAIL}Province not found.{bcolors.ENDC}\n")
                else:
                    break

            while True:
                newName = input("Enter a new name for the province: ")
                for i in provinces:
                    if newName == i["name"]:
                        print(f"{bcolors.FAIL}\nNew name can't be equal to an existing province.{bcolors.ENDC}\n")
                        break
                else:
                    provinces[provinceIndex]["name"] = newName
                    print(f"\n{bcolors.OKCYAN}Province name was updated to {newName}.{bcolors.ENDC}\n")
                    break
            ''' Delete province  '''
        elif option == 4:
            printCurrentProvinces()
            while True:
                repeatedProvince = False
                name = input("Enter province name to delete: ")
                for i in provinces:
                    if i["name"] == name:
                        repeatedProvince = True
                        provinceIndex = provinces.index(i)

                if repeatedProvince == True:
                    print(f"\n{bcolors.OKCYAN}Province {name} deleted successfully.{bcolors.ENDC}\n")
                    del provinces[provinceIndex]
                    break
                else:
                    print(f"\n{bcolors.FAIL}Province not found.{bcolors.ENDC}\n")
        
        elif option == 5:
            break
        
        else:
            print(f"\n{bcolors.FAIL}Invalid option. Please choose a number between 1 and 5.{bcolors.ENDC}\n")

# Function that executes a CRUD for cantons

def crudCanton():
    global provinces
    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}MANAGE CANTONS - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Create canton.")
        print(f"2. Display cantons list.")
        print(f"3. Update canton.")
        print(f"4. Delete canton.")
        print(f"5. Return to main menu.{bcolors.ENDC}")
        print("\n===================================================================================\n")
        
        option = generalFunctions.validateOption(5)
        ''' Following the menu. Request the name of the new canton and add it to the list of cantons '''
        if option == 1:
            repeatedCanton = False
            printCurrentProvinces()
            while True:
                repeatedProvince = False
                provinceName = input("Enter the name of the province to which the new canton will belong to: ")
                for i in range(0,len(provinces)):
                    if provinceName == provinces[i]["name"]:
                        repeatedProvince = True
                        provinceIndex = i
                        break
        
                if repeatedProvince == True:
                    break
                else:
                    print(f"\n{bcolors.FAIL}A province with this name doesn't exist.{bcolors.ENDC}\n")

            while True:
                repeatedCanton = False
                name = input("Introduce the name of the new canton: ")
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        if name == provinces[i]["cantons"][x]:
                                repeatedCanton = True
                if repeatedCanton == True:
                    print(f"\n{bcolors.FAIL}A canton with this name already exists.{bcolors.ENDC}\n")
                else:
                    provinces[provinceIndex]["cantons"].append(name)
                    print(f"\n{bcolors.OKCYAN}The new canton was added correctly.{bcolors.ENDC}\n")
                    break

            ''' Display cantons list '''
        elif option == 2:
            print("\nThis is the current list of cantons.\n")
            print("-----------------------------------------------------------------------------------")
            for i in range(0,len(provinces)):
                print(f"{bcolors.BOLD}Cantons in {provinces[i]['name']} province:{bcolors.ENDC}")
                print("-----------------------------------------------------------------------------------")
                for x in range(0,len(provinces[i]["cantons"])):
                    print(provinces[i]["cantons"][x])
                print("-----------------------------------------------------------------------------------")
                
            ''' Update canton (verify if canton exists) '''
        elif option == 3:
            printCurrentCantons()
    
            while True:
                repeatedCanton = False
                name = input("Enter the name of the canton you want to update: ")
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        if name == provinces[i]["cantons"][x]:
                            repeatedCanton = True
                            provinceIndex = i
                            cantonIndex = x
                if repeatedCanton == True:
                    break
                else:
                    print(f"\n{bcolors.FAIL}A canton with this name doesn't exist.{bcolors.ENDC}\n")

            while True:
                cantons = []
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        cantons.append(provinces[i]["cantons"][x])
                newName = input("Enter the new name for the canton: ")

                if newName in cantons:
                    print(f"\n{bcolors.FAIL}New name can't be equal to an existing canton.{bcolors.ENDC}\n")
                else:
                    provinces[provinceIndex]["cantons"][cantonIndex] = newName
                    print(f"\n{bcolors.OKCYAN}The name of the canton has been updated.\n{bcolors.ENDC}")
                    break
            ''' Delete canton '''
        elif option == 4:
            printCurrentCantons()

            while True:
                repeatedCanton = False
                name = input("Enter the name of the canton you want to delete: ")
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        if name == provinces[i]["cantons"][x]:
                            repeatedCanton = True
                            del provinces[i]["cantons"][x] 
                            print(f"\n{bcolors.OKCYAN}Canton deleted successfully.\n{bcolors.ENDC}")
                            break
                if repeatedCanton == True:
                    break
                else:
                    print(f"\n{bcolors.FAIL}A canton with this name doesn't exist.{bcolors.ENDC}\n")

            ''' Return to main menu '''
        elif option == 5:
            break

        else:
            print(f"\n{bcolors.FAIL}Invalid option. Please choose a number between 1 and 5. \n {bcolors.ENDC}")

# Function that displays reports menu 

def reportsMenu():
    while True:
        print("\n===================================================================================")
        print(f"{bcolors.BOLD}REPORTS - {bcolors.ENDC}{generalFunctions.printUserInfo()}")
        print("===================================================================================\n")
        print(f"{bcolors.OKCYAN}1. Cantons in alphabetical order.")
        print(f"2. Users by ascending age.")
        print(f"3. Quantity of women and men.")
        print(f"4. Quantity of men by province.")
        print(f"5. Quantity of women by canton.")
        print(f"6. Vehicles by type.")
        print(f"7. Pending approval events with a fine higher than 45 000 colones.")
        print(f"8. Closed events.")
        print(f"9. Open events by hour.")
        print(f"10. Province with the highest and lowest number of events.")
        print(f"11. Return to main menu.{bcolors.ENDC}")
        print("\n===================================================================================\n")
        
        option = generalFunctions.validateOption(11)

        if option == 1:
            generateReportOne()
        elif option == 2:
            generateReportTwo()
        elif option == 3:
            generateReportThree()
        elif option == 4:
            generateReportFour()
        elif option == 5:
            generateReportFive()
        elif option == 6:
            generateReportSix()
        elif option == 7:
            generateReportSeven()
        elif option == 8:
            generateReportEight()
        elif option == 9:
            generateReportNine()
        elif option == 10:
            generateReportTen()
        elif option == 11:
            break

# Function that generates the report number one (cantons in alphabetical order)
''' Using the sorted function returns the provinces (scrolls through the list of provinces) in alphabetical order '''
def generateReportOne():

    global provinces

    cantonsAlphabeticOrder = []

    for i in range(0, len(provinces)):
        for x in range(0, len(provinces[i]["cantons"])):
            cantonsAlphabeticOrder.append(provinces[i]["cantons"][x])

    cantonsAlphabeticOrder = sorted(cantonsAlphabeticOrder)

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Cantons in alphabetical order{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")
    for i in cantonsAlphabeticOrder:
        print(i)
    print("-----------------------------------------------------------------------------------")

# Function that generates the report number two (users by ascending age)
''' Using the sorted anf key=lamba function returns a list created where the users are sorted in ascending order by their age'''
def generateReportTwo():

    global users

    arrangedUsers = sorted(users, key=lambda person: person["age"])

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Users by ascending age{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")
    for person in arrangedUsers:
        print(f"Age: {person['age']}, Name: {person['name']}, Profile: {person['profile']}. ")
    print("-----------------------------------------------------------------------------------")

# Function that generates the report number three (quantity of women and men)
''' Starts two variables at cero and goes through the list of users, which depending on the gender increment the value'''
def generateReportThree():

    global users

    women = 0
    men = 0

    for i in range(0, len(users)):
        if users[i]["gender"] == "female":
            women += 1
        else:
            men += 1

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Quantity of women and men{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")
    print(f"Current quantity of male users in the system: {men}.")
    print(f"Current quantity of female users in the system: {women}.")
    print("-----------------------------------------------------------------------------------")

# Function that generates the report number four (quantity of men by province)

def generateReportFour():

    global users, provinces

    printCurrentProvinces()

    while True:
        repeatedProvince = False
        provinceName = input("Enter the name of the province in order to display its quantity of men: ")
        for i in range(0,len(provinces)):
            if provinceName == provinces[i]["name"]:
                repeatedProvince = True
                provinceIndex = i
                break

        if repeatedProvince == True:
            break
        else:
            print(f"\n{bcolors.FAIL}A province with this name doesn't exist.{bcolors.ENDC}\n")

    men = 0
    for x in range(0, len(users)):
        if users[x]["gender"] == "male":
            userResidency = users[x]["residency"].split(",")
            
            if userResidency[0] == provinces[provinceIndex]["name"]:
                men += 1
    
    print("\n-----------------------------------------------------------------------------------")
    print(f"Current quantity of men in {provinces[i]['name']} province: {men}.")
    print("-----------------------------------------------------------------------------------")

# Function that generates the report number five (quantity of women by canton)

def generateReportFive():

    global users, provinces

    printCurrentCantons()

    while True:
        repeatedCanton = False
        name = input("Enter the name of the canton in order to display its quantity of women: ")
        for i in range(0,len(provinces)):
            for x in range(0,len(provinces[i]["cantons"])):
                if name == provinces[i]["cantons"][x]:
                    repeatedCanton = True
                    cantonIndex = x
                    provinceIndex = i
        if repeatedCanton == True:
            break
        else:
            print(f"\n{bcolors.FAIL}A canton with this name doesn't exist.{bcolors.ENDC}\n")

    women = 0
    for x in range(0, len(users)):
        if users[x]["gender"] == "female":
            userResidency = users[x]["residency"].split(", ")
            
            if userResidency[1] == provinces[provinceIndex]["cantons"][cantonIndex]:
                women += 1
        
    print("\n-----------------------------------------------------------------------------------")
    print(f"Current quantity of women in {provinces[provinceIndex]['cantons'][cantonIndex]} canton: {women}.")
    print("-----------------------------------------------------------------------------------")

# Function that generates the report number six (vehicles by type)
''' Prints the vehicles by type in the list created'''
def generateReportSix():

    global vehicles

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Vehicles by type{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")
    print(f"Current list of 'motorcycle' type vehicles:")

    for i in vehicles:
        if i["type"] == "motorcycle":
            print(f"Number plate: {i['numberPlate']}, Brand: {i['brand']}.")
    print("")

    print(f"Current list of 'automobile' type vehicles:")

    for i in vehicles:
        if i["type"] == "automobile":
            print(f"Number plate: {i['numberPlate']}, Brand: {i['brand']}.")
    print("")

    print(f"Current list of 'bus' type vehicles:")

    for i in vehicles:
        if i["type"] == "bus":
            print(f"Number plate: {i['numberPlate']}, Brand: {i['brand']}.")
    print("")

    print(f"Current list of 'truck' type vehicles:")

    for i in vehicles:
        if i["type"] == "truck":
            print(f"Number plate: {i['numberPlate']}, Brand: {i['brand']}.")

    print("-----------------------------------------------------------------------------------")


# Function that generates the report number seven (pending approval events with a fine higher than 45 000 colones)
''' Prints the pending approval events with a fine higher than 45 000 colones in the list created'''
def generateReportSeven():
    
    global events

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Pending approval events with a fine higher than 45 000 colones{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")

    for i in events:
        if i.fine >= 45000 and i.status == "pending approval":
            print(f"Code: {i.code}, Police officer name: {i.officerName}, Fine: {i.fine}.")

    print("-----------------------------------------------------------------------------------")

# Function that generates the report number eight (closed events)
''' Prints the closed events in the list created within a txt file'''
def generateReportEight():
    
    global events, closedEvents

    judgeFunctions.writeClosedEventsOnFile()

    print(f"\n{bcolors.OKCYAN}Closed events list retrieved from 'closedEvents.txt' file.{bcolors.ENDC}\n")

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Closed events{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")

    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    closedEvents = []

    with open(os.path.join(__location__, "closedEvents.txt"), 'r') as f:
        for i in f:
            parameters = i.split(", ")
            closedEvent = Event(int(parameters[0]), parameters[1], (f"{parameters[2]}, {parameters[3]}"), parameters[4], parameters[5], datetime.strptime(parameters[6], "%Y-%m-%d %H:%M:%S"), float(parameters[7]), int(parameters[8]), parameters[9], int(parameters[10]), parameters[11])
            closedEvents.append(closedEvent)

        for i in closedEvents:
            print(f"Citizen name: {i.citizenName}, Penalty fee number: {i.penaltyFeeNumber}, Location: {i.location}, Status: {i.status.capitalize()}, Date-time: {i.dateTime}.")

    print("-----------------------------------------------------------------------------------")

# Function that generates the report number nine (open events by hour)
''' Prints the open events by hour less than the limit time in the list created'''
def generateReportNine():
    
    global events

    while True:
        format = "%H:%M:%S"
        limitTime = input("Introduce the limit time for the open events (hours:minutes:seconds) --> (00:00:00): ")
        try:
            bool(datetime.strptime(limitTime, format))
            break
        except:
            print(f"\n{bcolors.FAIL}Invalid input.{bcolors.ENDC}\n")

    limitTime = datetime.strptime(limitTime, format)        
        

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Open events by hour{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")

    for i in events:
        if i.status == "open" and (i.dateTime.time() < limitTime.time()):
            print(i.formatIfOpen())


    print("-----------------------------------------------------------------------------------")

# Function that generates the report number ten (province with the highest and lowest number of events)
''' Prints the province with the highest and lowest number of events in the list created, used split() function to separate 
the name and the number by province'''
def generateReportTen():
    
    global events, provinces

    highest = {
        "name":"",
        "number":-1
    }

    lowest = {
        "name":"",
        "number":999999999999999
    }

    for i in provinces:

        eventsQuantity = 0

        for x in events:
            divideLocation = (x.location).split(",")
            if divideLocation[0] == i["name"]:
                eventsQuantity += 1


        if eventsQuantity > highest["number"]:
            highest["number"] = eventsQuantity
            highest["name"] = i["name"]

        if eventsQuantity < lowest["number"]:
            lowest["number"] = eventsQuantity
            lowest["name"] = i["name"]

    print("\n-----------------------------------------------------------------------------------")
    print(f"{bcolors.BOLD}Province with the highest and lowest number of events{bcolors.ENDC}")
    print("-----------------------------------------------------------------------------------")

    print(f"Highest events quantity province: {highest['name']}, Events quantity: {highest['number']}.")
    print(f"Lowest events quantity province: {lowest['name']}, Events quantity: {lowest['number']}.")

    print("-----------------------------------------------------------------------------------")
    

    

