from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers.auth_routes import auth_bp
from controllers.admin_routes import admin_bp
from controllers.shared_routes import shared_bp
from models import db 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = 'a3f8b6e9c9d48f3ec1a7f2d3e6b1a2c4d5e6f7c8b9d0a1e2f3a4b5c6d7e8f9a0'

    # Lier SQLAlchemy à l'application Flask
    db.init_app(app)
    
 # Enregistrer les Blueprints
    app.register_blueprint(admin_bp, url_prefix='/admin')     # Routes spécifiques aux admins
    app.register_blueprint(shared_bp, url_prefix='/')   # Routes partagées (admin/agent)
    app.register_blueprint(auth_bp, url_prefix='/')       # Authentifications
    return app

app=create_app()

# Rediriger la racine "/" vers la page de connexion
@app.route('/')

def home():
    return redirect(url_for('auth.login_page'))  # Redirection vers /auth/login

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()  # Crée les tables dans la base de données
        print("Les tables ont été créées avec succès.")
    app.run(debug=True)
