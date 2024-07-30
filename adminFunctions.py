# Libraries
# ========================================================================================
import generalFunctions
from globalVariables import *
from datetime import datetime

# Function that displays the menu for admin profile

def menuAdmin():
    global currentUser,users,ids
    while True:
        print("\n")
        print("========================================================")
        print("1. Create user.")
        print("2. Manage provinces.")
        print("3. Manage cantons.")
        print("4. Reports.")
        print("5. Close session.")
        print("========================================================\n")

        option=int(input("Introduce a number: "))
        if option==1:
            pass
        elif option==2:
            crudProvince()
        elif option==3:
            pass
        elif option==4:
            pass
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
            print("New user created correctly. ")
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
        print("1. Create province.")
        print("2. Display province list.")
        print("3. Update province.")
        print("4. Delete province.")
        print("5. Return to main menu.")
        print("========================================================\n")
        
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