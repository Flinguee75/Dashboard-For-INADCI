import numpy as np
import pandas as pd
import joblib
import math
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# *** Chargement des fichiers nécessaires ***
def load_files():
    # Construire les chemins absolus pour les fichiers
    paths = {
        "model": os.path.join(BASE_DIR, "ia", "final_model.pkl"),
        
        "preprocessor": os.path.join(BASE_DIR, "ia", "preprocessor.pkl"),
        "features": os.path.join(BASE_DIR, "ia", "features_names.pkl"),
        "selected_features": os.path.join(BASE_DIR, "ia", "selected_features.pkl"),
    }
    
     # Vérifier si les fichiers existent
    for key, path in paths.items():
        if os.path.isfile(path):
            print(f"{key}: {path} exists.")
        else:
            print(f"{key}: {path} does NOT exist.")

    # Charger les fichiers
    try:
        final_model = joblib.load(paths["model"])
        print("Modèle chargé avec succès.")

        preprocessor = joblib.load(paths["preprocessor"])
        print("Préprocesseur chargé avec succès.")

        feature_names = joblib.load(paths["features"])
        print("Noms des caractéristiques chargés avec succès.")

        selected_features = joblib.load(paths["selected_features"])
        print("Selected features chargées avec succès.")

        return final_model, preprocessor, feature_names, selected_features
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        print("Assurez-vous que les fichiers sont dans le même répertoire que ce script.")
        raise


# *** Prétraitement des données utilisateur ***
def preprocess_input(form_data, preprocessor, feature_names, selected_features):
    # Construire un tableau avec les données utilisateur
    input_data = np.array([[
        form_data.get('nom_region', ''),
        form_data.get('nom_espece', ''),
        form_data.get('superficie', 0),
        form_data.get('pluviometrie', 0),
        form_data.get('annee', 2019),
        form_data.get('temperature_moyenne', 0),
        form_data.get('mois_plantation', 1),
        form_data.get('log_pluviometrie', 0),
        form_data.get('categorie_pluviometrie', 'Moyenne')
    ]])

    # Convertir en DataFrame avec les colonnes nécessaires
    input_df = pd.DataFrame(input_data, columns=feature_names)

    # Appliquer le préprocesseur
    input_transformed = preprocessor.transform(input_df)

    # Convertir les noms de colonnes en indices si nécessaire
    if isinstance(selected_features[0], str):
        feature_indices = [list(preprocessor.get_feature_names_out()).index(col) for col in selected_features]
    else:
        feature_indices = selected_features

    # Sélectionner les colonnes dans la matrice transformée
    input_transformed = input_transformed[:, feature_indices]

    return input_transformed


# *** Fonction principale ***
def predict(user_data):
    # Charger les fichiers nécessaires
    final_model, preprocessor, feature_names, selected_features = load_files()


    # Calcul des colonnes supplémentaires
    user_data['log_pluviometrie'] = math.log(user_data['pluviometrie'])

    # Définir les catégories de pluviométrie
    bins = [0, 100, 200, 300, float('inf')]
    labels = ['Faible', 'Moyenne', 'Élevée', 'Très Élevée']
    user_data['categorie_pluviometrie'] = pd.cut(
        [user_data['pluviometrie']], bins=bins, labels=labels
    )[0]

    # Prétraiter les données utilisateur
    input_transformed = preprocess_input(user_data, preprocessor, feature_names, selected_features)

    # Faire la prédiction
    rendement_tonnes = final_model.predict(input_transformed)[0]

    return rendement_tonnes

