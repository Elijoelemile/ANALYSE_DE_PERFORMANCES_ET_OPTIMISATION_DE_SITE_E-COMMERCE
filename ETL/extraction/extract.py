import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialisation de l'API (va chercher kaggle.json automatiquement)
api = KaggleApi()
api.authenticate()

# Nom du dataset (slug pris de l’URL Kaggle)
dataset = "retailrocket/ecommerce-dataset"

# Destination de téléchargement (ton projet)
destination_dir = r"C:\Users\Эли Жоэль\ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE\data\raw"

os.makedirs(destination_dir, exist_ok=True)

# Téléchargement et décompression
api.dataset_download_files(dataset, path=destination_dir, unzip=True)

print(f"Dataset téléchargé dans : {destination_dir}")
