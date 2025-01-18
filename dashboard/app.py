from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers.auth_routes import auth_bp
from controllers.admin_routes import admin_bp
from models import db 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Lier SQLAlchemy à l'application Flask
    db.init_app(app)
    
    # Enregistrer les blueprints
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(admin_bp, url_prefix='/admin')  # Préfixe pour les routes Admin

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
