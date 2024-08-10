
# User management
# ===================================================================================================================

# Predifined users

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

users = [administrator, isabel, angelica, raul, citizen]

# Current user logged in the system info

currentUser = 1
currentUserName = ''
currentUserProfile = ''
currentUserID = ''

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

events = []

class Event:
    def __init__(self, code, citizenName, location, carPlate, status, dateTime, fee):
        self.code = code
        self.citizenName = citizenName
        self.location = location
        self.carPlate = carPlate
        self.status = status
        self.dateTime = dateTime
        self.fee = fee

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
    "ownerID":"222222222",
    "numberPlate":"QWE-123",
    "year":"2018",
    "brand":"Honda",
    "color":"red",
    "type":"motorcycle"
}

vehicles = [vehicle01, vehicle02]

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

