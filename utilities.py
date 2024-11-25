import requests
import json
import os  # Utilisé pour gérer les répertoires
# Utilisé pour générer l'horodatage dans le nom des fichiers json
from datetime import datetime


class Meteo:
    """
    Classe permettant de récupérer et de traiter
    les prévisions météo pour une ville donnée.
    """

    def __init__(self):
        """
        Initialise une instance de la classe Meteo
        avec les informations utilisateur.
        Demande à l'utilisateur d'entrer une ville et un pays
        pour lesquels récupérer les données météo.
        Définit l'URL de l'API et les paramètres associés.
        """
        # Ville entrée par l'utilisateur
        self.city = str(input('Enter the city you want: '))
        # Pays entré par l'utilisateur
        self.country = str(input('In which country it is: '))
        # clé API
        self.apiKey = "2257179fed7d3904654343d838db3f81"
        # URL pour la requête
        self.url = f'https://api.openweathermap.org/data/2.5/forecast?q={self.city},{self.country}&units=metric&appid={self.apiKey}'
        # Chemin vers un certificat personnalisé
        self.REQUESTED_CA_BUNDLE = 'airbus-ca.crt'

    def send_request(self):
        """
        Envoie une requête HTTP à l'API OpenWeatherMap
        pour obtenir les prévisions météo.

        :return: La réponse brute de l'API sous forme d'objet HTTP.
        """
        response = requests.get(self.url, verify=self.REQUESTED_CA_BUNDLE)
        response.raise_for_status()
        return response

    def verif_JSON(self, response):
        """
        Vérifie si la réponse obtenue de l'API est bien au format JSON.

        :param response: réponse de l'API.
        :return: Les données JSON si valides, None sinon.
        """
        try:
            return response.json()
        except ValueError:
            print("Invalid JSON format in the response.")
            return None

    def extract_forecast(self, data):
        """
        Extrait les prévisions météo des 5 prochains jours
        et les structure de manière lisible.

        :param data: Données au format JSON obtenues par l'API
        :return: Un dictionnaire contenant les prévisions météo formatées.
        """
        if not data or 'list' not in data or 'city' not in data:
            print("Malformed or missing data.")
            return None

        # Structure du fichier json
        forecast_details = {}
        city_name = data["city"]["name"]
        country = data["city"]["country"]
        forecast_details["forecast_location"] = f"{city_name}({country})"

        # Variables pour calculer les températures minimales et maximales
        min_temp = float('inf')
        max_temp = float('-inf')

        # Dictionnaire pour les données journalières
        daily_data = {}

        for entry in data['list']:
            date = entry['dt_txt'].split(" ")[0]  # Récupère la date
            temp = entry['main']['temp']

            # Mise à jour des températures minimales et maximales
            min_temp = min(min_temp, temp)
            max_temp = max(max_temp, temp)

            # Ajout des données à la date correspondante
            if date not in daily_data:
                daily_data[date] = {"temp_sum": 0, "count": 0}
            daily_data[date]["temp_sum"] += temp
            daily_data[date]["count"] += 1

        # Ajout des températures globles au dictionnaire principal
        forecast_details["forecast_min_temp"] = round(min_temp, 1)
        forecast_details["forecast_max_temp"] = round(max_temp, 1)

        # Construction de la liste des détails journaliers
        forecast_details["forecast_details"] = [
            {
                "date": date,
                "temp": round(values["temp_sum"] / values["count"], 1),
                "measure_count": values["count"],
            }
            for date, values in daily_data.items()
        ]

        return forecast_details

    def save_json_to_file(self, data):
        """
        Sauvegarde les prévisions météo formatées dans un fichier JSON
        Le fichier est enregistré dans le répertoire results

        :param data: Les données météo formatées sous forme de dictionnaire
        """
        if data:
            try:
                # Création du répertoire "results" s'il n'existe pas
                results_dir = "results"
                os.makedirs(results_dir, exist_ok=True)

                # Nom du fichier basé sur l'horodatage actuel
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_name = f"{results_dir}/{timestamp}.json"

                # Écriture des données dans le fichier JSON
                with open(file_name, 'w') as jsonfile:
                    json.dump(data, jsonfile, indent=4)
                print(f"Data saved successfully to {file_name}.")
            except IOError as e:
                print(f"Error saving the data: {e}")
        else:
            print("No data to save.")
