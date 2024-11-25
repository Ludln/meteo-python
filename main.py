# Importation de la classe Meteo pour gérer les prévisions météo
from utilities import Meteo

if __name__ == "__main__":
    """
    Crée une instance de la classe Meteo, récupère les prévisions météo,
    vérifie si la réponse est au format JSON
    et sauvegarde les données dans un fichier
    """

    # Création d'une instance de la classe Meteo
    meteo = Meteo()

    # Envoi de la requête HTTP pour récupérer les données météo
    # Cette méthode sert à récupérer les données de l'API OpenWeatherMap
    response = meteo.send_request()

    # Vérifie que la réponse est bien au format JSON
    # Si la réponse est au format JSON,
    # elle est retournée sous forme de dictionnaire
    data = meteo.verif_JSON(response)
    # Extraire et sauvegarder les données formatées
    if data:
        formatted_data = meteo.extract_forecast(data)
        meteo.save_json_to_file(formatted_data)
