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
        :param fileJson: chemin vers le fichier Json
        """

        self.city = str(input('Enter the city you want : '))
        self.country = str(input('In wich county it is : '))
        self.apiKey = "2257179fed7d3904654343d838db3f81"
        self.url = f'https://api.openweathermap.org/data/2.5/forecast?q={self.city},{self.country}&units=metric&appid={self.apiKey}'
        self.REQUESTED_CA_BUNDLE = 'airbus-ca.crt'
        self.fileJson = "test.json"

#############################################################################################################################################

    def send_request(self):
        """
        Envoie la requête HTTP pour récupérer les données météo.
        """
        response = requests.get(self.url, verify=self.REQUESTED_CA_BUNDLE)
        response.raise_for_status()  # Gère les erreurs HTTP (4xx et 5xx)
                
        if response.status_code == 404:
            print(">>> City or country not existing.")
                
        return response


    def verif_JSON(self, response):
        """
        Vérifie si la réponse est bien au format JSON.

        :param response: La réponse HTTP à vérifier
        :return: Les données JSON si le format est correct, None sinon
        """
        try:
            data = response.json()  # Tente de convertir la réponse en JSON
            return data
        except ValueError:
            print("La réponse n'est pas au format JSON ou est invalide.")
            return None


    def save_json_to_file(self, data):
        """
        Enregistre les données JSON dans un fichier.

        :param data: Les données JSON à sauvegarder
        """
        if data:
            try:
                with open(self.fileJson, 'w') as jsonfile:
                    json.dump(data, jsonfile, indent=4)  # Envoie des données dans le fichier
                print(f"Données sauvegardées dans {self.fileJson}.")
            except IOError as e:
                print(f"Erreur lors de la sauvegarde des données : {e}")
        else:
            print("Aucune donnée JSON n'a été récupérée.")


# Exemple d'utilisation
# if __name__ == "__main__":
#     objet = Meteo(10, "texte")
#     objet.methode_exemple()
#     resultat = objet.methode_calcul(5)
#     print(f"Résultat du calcul : {resultat}")
