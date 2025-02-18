from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from models.user_model import User

auth_bp = Blueprint('auth', __name__)

# Route pour afficher la page de connexion
@auth_bp.route('/login', methods=['GET'])

def login_page():
    return render_template('utilisateurs/login.html')

@auth_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('utilisateurs/register.html')

# Route pour traiter la connexion
@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # Vérifie si l'utilisateur existe
    user = User.query.filter_by(email=email).first()
    
    print("Hash stocké :", user.password)
    print("Mot de passe fourni :", password)
    print("Check hash :", check_password_hash(user.password, password))
    
    if not user or not check_password_hash(user.password, password):
        print("E-mail ou mot de passe incorrect")
        return render_template('utilisateurs/login.html', message="E-mail ou mot de passe incorrect")
    
    # Stocke les informations de session
    session['email'] = user.email
    session['role'] = user.role
    
    return redirect(url_for('shared.dashboard'))  # Redirige vers le tableau de bord admin
   


# Route pour se déconnecter
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Efface toutes les informations de session
    return redirect(url_for('auth.login_page'))  # Redirige vers la page de connexion