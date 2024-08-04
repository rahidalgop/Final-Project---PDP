
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
    "birthdate":"february"
}

isabel = {
    "id":"604840803",
    "name":"Isabel María Martínez Vindas",
    "password":"123",
    "profile":"citizen",
    "gender":"female",
    "age":20,
    "residency":"Alajuela, San Carlos",
    "birthdate":"february"
}

angelica = {
    "id":"208480382",
    "name":"Angélica Varela Vargas",
    "password":"456",
    "profile":"police officer",
    "gender":"female",
    "age":20,
    "residency":"Alajuela, San Carlos",
    "birthdate":"november"
}

raul = {
    "id":"207820653",
    "name":"José Raúl Hidalgo Pérez",
    "password":"789",
    "profile":"judge",
    "gender":"male",
    "age":25,
    "residency":"Alajuela, San Carlos",
    "birthdate":"august"
}

users = [administrator, isabel, angelica, raul]

# Current user logged in the system info

currentUser = 1
currentUserName = ''
currentUserProfile = ''

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

provinces = [alajuela,heredia,sanJose,puntarenas]

# Classes
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

