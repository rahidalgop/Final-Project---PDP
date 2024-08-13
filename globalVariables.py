
# User management
# ===================================================================================================================

# Predefined users

administrator = {
    "id":"000000000",
    "name":"John Doe",
    "password":"000",
    "profile":"administrator",
    "gender":"male",
    "age":35,
    "residency":"San José, Moravia",
    "birthdate":"10/06/1990"
}

isabel = {
    "id":"604840803",
    "name":"Isabel María Martínez Vindas",
    "password":"123",
    "profile":"citizen",
    "gender":"female",
    "age":20,
    "residency":"Alajuela, San Carlos",
    "birthdate":"10/06/1990"
}

angelica = {
    "id":"208480382",
    "name":"Angélica Varela Vargas",
    "password":"456",
    "profile":"police officer",
    "gender":"female",
    "age":20,
    "residency":"Alajuela, San Carlos",
    "birthdate":"10/06/1990"
}

raul = {
    "id":"207820653",
    "name":"José Raúl Hidalgo Pérez",
    "password":"789",
    "profile":"judge",
    "gender":"male",
    "age":25,
    "residency":"Alajuela, San Carlos",
    "birthdate":"10/06/1990"
}

citizen = {
    "id":"111111111",
    "name":"Mark Hoppus",
    "password":"111",
    "profile":"citizen",
    "gender":"male",
    "age":32,
    "residency":"Alajuela, San Carlos",
    "birthdate":"10/06/1990"
}

officer = {
    "id":"222222222",
    "name":"Tom DeLonge",
    "password":"222",
    "profile":"police officer",
    "gender":"male",
    "age":47,
    "residency":"Puntarenas, Esparza",
    "birthdate":"10/06/1990"
}

judge = {
    "id":"333333333",
    "name":"Travis Barker",
    "password":"333",
    "profile":"judge",
    "gender":"male",
    "age":62,
    "residency":"Heredia, Barva",
    "birthdate":"10/06/1990"
}

users = [administrator, isabel, angelica, raul, citizen, officer, judge]

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

class Event:
    def __init__(self, code, citizenName, location, numberPlate, status, dateTime, fine, infringementNumber, officerName, registerNumber, judgeName):
        self.code = code
        self.citizenName = citizenName
        self.location = location
        self.numberPlate = numberPlate
        self.status = status
        self.dateTime = dateTime
        self.fine = fine
        self.infringementNumber = infringementNumber
        self.officerName = officerName
        self.registerNumber = registerNumber
        self.judgeName = judgeName

    # def __str__(self) -> str:
    #     return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}."

    def formatIfOpen(self):
        return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}."

    def formatIfPendingApproval(self):
        return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}, Infringement number: {self.infringementNumber}, Police officer name: {self.officerName}."

    def formatIfClosed(self):
        return f"Code: {self.code}, Citizen full name: {self.citizenName}, Location: {self.location}, Involved vehicle: {self.numberPlate}, Status: {self.status.capitalize()}, Date-time: {self.dateTime}, Fine: {self.fine}, Infringement number: {self.infringementNumber}, Police officer name: {self.officerName}, Register number: {self.registerNumber}, Judge name: {self.judgeName}."

    def formatToFile(self):
        return f"{self.code}, {self.citizenName}, {self.location}, {self.numberPlate}, {self.status} {self.dateTime}, {self.fine}, {self.infringementNumber}, {self.officerName}, {self.registerNumber}, {self.judgeName}\n"

event01 = Event(12345, "Mark Hoppus", "Alajuela, San Carlos", "AAA-111", "open", "10/08/2024 18:45", 32500, '', '', '', '')

events = [event01]

# Vehicle management
# ===================================================================================================================

vehicle01 = {
    "ownerID":"111111111",
    "numberPlate":"AAA-111",
    "year":"2015",
    "brand":"Toyota",
    "color":"white",
    "type":"automobile"
}

vehicle02 = {
    "ownerID":"111111111",
    "numberPlate":"BBB-222",
    "year":"2018",
    "brand":"Honda",
    "color":"red",
    "type":"motorcycle"
}

vehicle03 = {
    "ownerID":"604840803",
    "numberPlate":"QWE-123",
    "year":"1980",
    "brand":"BMW",
    "color":"blue",
    "type":"truck"
}

vehicle04 = {
    "ownerID":"111111111",
    "numberPlate":"CCC-333",
    "year":"1997",
    "brand":"Kia",
    "color":"yellow",
    "type":"motorcycle"
}

vehicles = [vehicle01, vehicle02, vehicle03, vehicle04]

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

