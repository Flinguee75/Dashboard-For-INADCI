
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Le chemin de la base de données pointe vers le dossier `data`
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "data", "mydb.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
