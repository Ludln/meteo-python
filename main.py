import requests
import json
from datetime import datetime

from utilities import Meteo  # Importer la classe Meteo

if __name__ == "__main__":
    # Créer une instance de la classe Meteo
    meteo = Meteo()  # L'utilisateur entre la ville et le pays ici
    response = meteo.send_request()  # Utiliser la méthode send_request via l'instance
    data = meteo.verif_JSON(response)  # Vérifier que la réponse est au format JSON
    
    # Sauvegarder les données JSON si elles sont valides
    meteo.save_json_to_file(data)






    # -m pip install