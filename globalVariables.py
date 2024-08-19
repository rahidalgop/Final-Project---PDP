# Libraries
# ===================================================================================================================

from datetime import datetime

# User management
# ===================================================================================================================
''' IMPORTANT! 
The data presented in this administration system are fictitious and only for testing purposes becasue is necesary to be 
able to define the other users in the system

In this part of the code will appear list with defined values but there're alse several empty lists that will store the data
we insert.'''
# Predefined users

administrator = {
    "id":"000000000",
    "name":"John Doe",
    "password":"000",
    "profile":"administrator",
    "gender":"male",
    "age":35,
    "residency":"San José, Moravia",
    "birthdate":"10/06"
}

users = [administrator]

# Current user logged in the system info

currentUser = 1
currentUserName = ''
currentUserProfile = ''
currentUserID = ''
currentUserVehicles = []

# Residency management
# ===================================================================================================================

# Provinces and cantons

alajuela = {
    "name": "Alajuela",
    "cantons": ["San Carlos", "Zarcero"]
}

heredia = {
    "name": "Heredia",
    "cantons": ["Barva", "Belén"]
}

sanJose = {
    "name": "San José",
    "cantons": ["Tibás", "Moravia"]
}

puntarenas = {
    "name": "Puntarenas",
    "cantons": ["Esparza", "Buenos Aires"]
}

provinces = [alajuela, heredia, sanJose, puntarenas]

# Event management
# ===================================================================================================================
''' Events simply return strings with the information of the event corresponding to the specified user(all details). '''
class Event:
    def __init__(self, code, citizenName, location, numberPlate, status, dateTime, fine, penaltyFeeNumber, officerName, registerNumber, judgeName):
        self.code = code
        self.citizenName = citizenName
        self.location = location
        self.numberPlate = numberPlate
        self.status = status
        self.dateTime = dateTime
        self.fine = fine
        self.penaltyFeeNumber = penaltyFeeNumber
        self.officerName = officerName
        self.registerNumber = registerNumber
        self.judgeName = judgeName

    # def __str__(self) -> str:
    #     return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}."

    def formatIfOpen(self):
        return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}."

    def formatIfPendingApproval(self):
        return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}, Penalty fee number: {self.penaltyFeeNumber}, Police officer name: {self.officerName}."

    def formatIfClosed(self):
        return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}, Penalty fee number: {self.penaltyFeeNumber}, Police officer name: {self.officerName}, Register number: {self.registerNumber}, Judge name: {self.judgeName}."

    def formatToFile(self):
        return f"{self.code}, {self.citizenName}, {self.location}, {self.numberPlate}, {self.status}, {self.dateTime}, {self.fine}, {self.penaltyFeeNumber}, {self.officerName}, {self.registerNumber}, {self.judgeName}\n"

events = []

closedEvents = []

# Vehicle management
# ===================================================================================================================

''' This list contains all the vehicles in the system. '''
vehicles = []

vehicleBrands = ["Toyota", "Ford", "Volkswagen", "Nissan", "BMW", "Chevrolet", "Honda", "Hyundai", "Kia", "Other"]
vehicleColors = ["white", "gray", "black", "blue", "silver", "red", "green", "yellow", "orange", "other"]

# Interface / aesthetics
# ===================================================================================================================

# Color to implement to the terminal text

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

