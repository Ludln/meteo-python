import requests
import json
from datetime import datetime


class Meteo :

    def __init__(self):
        """
        Class constructor.

        :param city: Ville dont on veut le forecast
        :param country: Pays de la ville dont on veut le forecast
        :param apiKey: clé API
        :param url: URL de l'API
        :param REQUESTED_CA_BUNDLE: certificat
        """

        self.city = str(input('Enter the city you want : '))
        self.country = str(input('In wich county it is : '))
        self.apiKey = "2257179fed7d3904654343d838db3f81"
        self.url = f'https://api.openweathermap.org/data/2.5/forecast?q={self.city},{self.country}&units=metric&appid={self.apiKey}'
        self.REQUESTED_CA_BUNDLE = 'airbus-ca.crt'

#############################################################################################################################################

    def send_request(self):
        """
        Envoie de la requête
        """
        response = requests.get(f"{self.url}", verify=self.REQUESTED_CA_BUNDLE)
        if response.status_code == 404:                     # Si le status code de la requête est 404,
            print (">>>", "City or country not existing.")  # l'utilisateur est informé que les informations rentrées sont incorrectes
        return response


    def verif_JSON(self, response):
        """
            Vérifie si la réponse est bien au format JSON
        """
        try:
            data = response.json()  
        except ValueError:
            print("La réponse n'est pas en format JSON.")
            data = None
        if data:
            with open('test.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Envoie des données dans "test.json"
        else:
            print("Aucune donnée JSON n'a été récupérée.")


# Exemple d'utilisation
if __name__ == "__main__":
    objet = Meteo(10, "texte")
    objet.methode_exemple()
    resultat = objet.methode_calcul(5)
    print(f"Résultat du calcul : {resultat}")
