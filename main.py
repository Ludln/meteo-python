import requests
import json
from datetime import datetime


apiKey = "2257179fed7d3904654343d838db3f81"

# Récupération des paramètres
city = str(input('Enter the city you want : '))
country = str(input('In wich county it is : '))

# URL de l'API
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city},{country}&units=metric&appid={apiKey}'

# Certificat
REQUESTED_CA_BUNDLE = 'airbus-ca.crt'

# Envoie de la requête
response = requests.get(f"{url}", verify=REQUESTED_CA_BUNDLE)
if response.status_code == 404:                     # Si le status code de la requête est 404,
    print (">>>", "City or country not existing.")  # l'utilisateur est informé que les informations rentrées sont incorrectes

try:
    data = response.json()  # Vérifie si la réponse est bien au format JSON
except ValueError:
    print("La réponse n'est pas en format JSON.")
    data = None

# Si la réponse est au format JSON, elle est enregistré dans le fichier "test.json"
if data:
    with open('test.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)  # Envoie des données dans "test.json"
else:
    print("Aucune donnée JSON n'a été récupérée.")


















    # -m pip install