
# Libraries
# ========================================================================================
import generalFunctions
from globalVariables import *
from datetime import datetime

# Function that displays the menu for admin profile

def menuAdmin():
    global currentUser,users,ids
    while True:
        print("\n========================================================")
        print("MAIN MENU")
        print("========================================================\n")
        print("1. Create user.")
        print("2. Manage provinces.")
        print("3. Manage cantons.")
        print("4. Reports.")
        print("5. Close session.")
        print("\n========================================================\n")

        option=int(input("Introduce a number: "))
        if option==1:
            createNewUser()
        elif option==2:
            crudProvince()
        elif option==3:
            crudCanton()
        elif option==4:
            reportsMenu()
        elif option==5: 
            generalFunctions.closeSession()
            break
        else:
            print("error")
            break

# Function that creates a new user

def createNewUser():
    global users
    while True:
        idInUse = False
        newUserID = input("Introduce user's ID: ")
        try:
            newUserID = int(newUserID)
            newUserID = str(newUserID)
            if len(newUserID) != 9:
                print("ID length must be equal to nine. ")
            if len(newUserID) == 9:
                for i in range(0, len(users)):
                    if users[i]["id"] == newUserID:
                        idInUse = True
                if idInUse == True:
                    print("ID is currently assigned to another user. ")
                else:
                    break
        except ValueError:
            print("ID length must be equal to nine and must only contain numerical characters. ")

    newUserName = input("Introduce user's full name: ")
    newUserResidency = input("Introduce user's residency: ")
    newUserAge = input("Introduce user's age: ")
    while True:
        try:
            newUserAge = int(newUserAge)
            break
        except ValueError:
            print("Age must only contain numerical characters.")
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
            print("Invalid input.")
    while True:
        format = "%d/%m/%Y"
        newUserBirthdate = input("Introduce user's birthdate (DD/MM/YYYY): ")
        try:
            validFormat = bool(datetime.strptime(newUserBirthdate, format))
            break
        except:
            validFormat = False
            print("Invalid input.")

    while True:
        newUserPassword = input("Introduce user's password: ")
        newUserValidatePassword = input("Confirm user's password: ")
        if newUserPassword == newUserValidatePassword:
            break
        else:
            print("Passwords do not match. ")

    while True:
        print("Select a profile for the user.")
        print("\n1. Administrator.")
        print("2. Citizen.")
        print("3. Police officer.")
        print("4. Judge.\n")
        profileOption = input("Introduce a number: ")

        try:
            profileOption = int(profileOption)
            if profileOption == 1 or profileOption == 2 or profileOption == 3 or profileOption == 4:
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")

    if profileOption == 1:
        newUserProfile = "administrator"
    elif profileOption == 2:
        newUserProfile = "citizen"
    elif profileOption == 3:
        newUserProfile = "police"
    elif profileOption == 4:
        newUserProfile = "judge"

    newUser = dict()
    newUser["id"] = newUserID
    newUser["name"] = newUserName
    newUser["password"] = newUserPassword
    newUser["age"] = newUserAge
    newUser["gender"] = newUserGender
    newUser["birthdate"] = newUserBirthdate
    newUser["profile"] = newUserProfile
    newUser["residency"] = newUserResidency

    users.append(newUser)
    print("The new user was created successfully.\n")
    for i in users:
        print(i)

# Function that executes a CRUD for provinces

def crudProvince():
    global provinces
    while True:
        print("\n========================================================")
        print("MANAGE PROVINCES")
        print("========================================================\n")
        print("\n1. Create province.")
        print("2. Display province list.")
        print("3. Update province.")
        print("4. Delete province.")
        print("5. Return to main menu.\n")
        print("\n========================================================\n")
        
        while True:
            try:
                option = int(input("Introduce a number: "))
                if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")


        if option == 1:
            while True:
                repeatedProvince = False
                name = input("Enter province name: ")
                for i in range(0,len(provinces)):
                    if name == provinces[i]["name"]:
                        repeatedProvince = True

                if repeatedProvince == True:
                    print("A province with this name already exists.")
                else:
                    break
            newProvince = dict()
            newProvince["name"] = name
            provinces.append(newProvince)
            print("The province was added correctly.")

        
        elif option == 2:
            print("This is the current list of the provinces.\n")
            for i in range(0,len(provinces)):
                print(provinces[i]["name"])

        
        elif option == 3:
            print("This is the current list of the provinces.\n")
            for i in range(0,len(provinces)):
                print(provinces[i]["name"])
            name = input("Enter province name to update: ")
            for i in provinces:
                if i["name"] == name:
                    newName = input("Enter new name for the province: ")
                    if newName != name and any(np["name"] == newName for np in provinces):
                        print("A province with this new name already exists.")
                    else:
                        i["name"] = newName
                        print(f"Province name updated to {newName}.")
                    break
            else:
                print("Province not found.")

        elif option == 4:
            print("This is the current list of the provinces.\n")
            for i in range(0,len(provinces)):
                print(provinces[i]["name"])
            name = input("Enter province name to delete: ")
            for idx, i in enumerate(provinces):
                if i["name"] == name:
                    del provinces[idx]
                    print(f"Province {name} deleted successfully.")
                    break
            else:
                print("Province not found.")
        
        elif option == 5:
            break
        
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

# Function that executes a CRUD for cantons

def crudCanton():
    global provinces
    while True:
        print("\n========================================================")
        print("MANAGE CANTONS")
        print("========================================================\n")
        print("1. Create canton.")
        print("2. Display canton list.")
        print("3. Update canton.")
        print("4. Delete canton.")
        print("5. Return to main menu.")
        print("\n========================================================\n")
        
        while True:
            try:
                option = int(input("Introduce a number: "))
                if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")

        if option == 1:
            repeatedCanton = False
            print("This is the current list of the provinces.\n")
            for i in range(0,len(provinces)):
                print(provinces[i]["name"])
            while True:
                repeatedProvince = False
                provinceName = input("Enter province name: ")
                for i in range(0,len(provinces)):
                    if provinceName == provinces[i]["name"]:
                        repeatedProvince = True
                        provinceIndex = i
                        break
        
                if repeatedProvince == True:
                    break
                else:
                    print("A province with this name doesn't exist.")

            repeatedCanton = False
            while True:
                name = input("Enter canton name: ")
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        if name == provinces[i]["cantons"][x]:
                                repeatedCanton = True
                if repeatedCanton == True:
                    print("A canton with this name already exists.")
                else:
                    provinces[provinceIndex]["cantons"].append(name)
                    print("The canton was added correctly.")
                    break
    
    
        elif option == 2:
            print("This is the current list of the cantons.\n")
            for i in range(0,len(provinces)):
                for x in range(0,len(provinces[i]["cantons"])):
                    print(provinces[i]["cantons"][x])
    

        elif option == 3:
            print("This is the current list of the cantons.\n")
            for i in range(0,len(provinces)):
                for x in range(0,len(provinces[i]["cantons"])):
                    print(provinces[i]["cantons"][x])
    

            while True:
                repeatedCanton = False
                name = input("\nEnter the name of the canton you want to update: ")
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        if name == provinces[i]["cantons"][x]:
                            repeatedCanton = True
                if repeatedCanton == True:
                    break
                else:
                    print("A canton with this name doesn't exist.")

            while True:
                newName = input("Enter new name for the canton: ")
                if newName != name:
                    for i in range(0,len(provinces)):
                        for x in range(0,len(provinces[i]["cantons"])):
                            if name == provinces[i]["cantons"][x]:
                                provinces[i]["cantons"][x] = newName
                                print("The name of the canton has been updated.")
                                break
                    break
                else:
                    print("The new name can't be equal to current name.")
            

        elif option == 4:
            print("This is the current list of the cantons.\n")
            for i in range(0,len(provinces)):
                for x in range(0,len(provinces[i]["cantons"])):
                    print(provinces[i]["cantons"][x])
    

            while True:
                repeatedCanton = False
                name = input("\nEnter the name of the canton you want to delete: ")
                for i in range(0,len(provinces)):
                    for x in range(0,len(provinces[i]["cantons"])):
                        if name == provinces[i]["cantons"][x]:
                            repeatedCanton = True
                if repeatedCanton == True:
                    break
                else:
                    print("A canton with this name doesn't exist.")
                
            for i in range(0,len(provinces)):
                for x in range(0,len(provinces[i]["cantons"])):
                    if name == provinces[i]["cantons"][x]:
                        del provinces[i]["cantons"][x] 
                        print("Canton deleted successfully.")

        elif option == 5:
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")



# Function that displays reports menu

def reportsMenu():
    while True:
        print("\n========================================================")
        print("REPORTS")
        print("========================================================\n")
        print("1. Cantons in alphabetical order.")
        print("2. Users by ascending age.")
        print("3. Quantity of women and men.")
        print("4. Men by province.")
        print("5. Women by canton.")
        print("6. Vehicles by type.")
        print("7. Pending approval events with a fine higher than 45 000 colones.")
        print("8. Completed events.")
        print("9. Open events by hour.")
        print("10. Province with the highest and lowest number of incidents.")
        print("11. Return to main menu.")
        print("\n========================================================\n")
        
        while True:
            try:
                option = int(input("Introduce a number: "))
                if option >= 1 and option <= 11 and option % 1 == 0:
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")

        if option == 1:
            generateReportOne()
        elif option == 2:
            pass
        elif option == 3:
            generateReportThree()
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        elif option == 10:
            pass
        elif option == 11:
            break

# Function that generates the report number one (cantons in alphabetical order)

def generateReportOne():

    global provinces

    cantonsAlphabeticOrder = []

    for i in range(0, len(provinces)):
        for x in range(0, len(provinces[i]["cantons"])):
            cantonsAlphabeticOrder.append(provinces[i]["cantons"][x])

    cantonsAlphabeticOrder = sorted(cantonsAlphabeticOrder)

    print("\n--------------------------------------------------------")
    print("List of cantons in alphabetical order.")
    print("--------------------------------------------------------")

    for i in cantonsAlphabeticOrder:
        print(i)

    print("--------------------------------------------------------\n")

# Function that generates the report number three (quantity of women and men)

def generateReportThree():

    global users

    women = 0
    men = 0

    for i in range(0, len(users)):
        if users[i]["gender"] == "female":
            women += 1
        else:
            men += 1

    print("\n--------------------------------------------------------")
    print("Quantity of women and men.")
    print("--------------------------------------------------------")

    print(f"Current quantity of male users in the system: {men}")
    print(f"Current quantity of female users in the system: {women}")

    print("--------------------------------------------------------\n")
