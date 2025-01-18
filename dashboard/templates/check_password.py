
from flask import app
from models.user_model import User

with app.app_context():  # Nécessaire pour accéder à la base de données
    users = User.query.all()  # Récupérer tous les utilisateurs
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Role: {user.role}, Date Created: {user.date_created}")
