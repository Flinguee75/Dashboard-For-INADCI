from flask import Blueprint, redirect, render_template, request, jsonify, session, url_for
from models import db
from models import User
from werkzeug.security import generate_password_hash

# Création du Blueprint pour les routes Admin
admin_bp = Blueprint('admin', __name__)

# Route : Tableau de bord de l'administrateur
@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
      return render_template('tableau_de_bord/index.html')

# Route : Ajouter un utilisateur
@admin_bp.route('/add_user', methods=['GET'])
def add_user_form():
    return render_template('utilisateurs/register.html')

@admin_bp.route('/add_user', methods=['POST'])
def add_user():
    print("Ajout d'un utilisateur")
    email = request.form.get('email')  # Remplacez request.json par request.form
    password = request.form.get('password')
    role = request.form.get('role')

    # Vérifier les données
    if not email or not password or not role:
        return jsonify({'message': 'Les champs email, password et role sont obligatoires'}), 400

    # Vérifier si l'utilisateur existe déjà
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Cet utilisateur existe déjà'}), 400

    # Ajouter un nouvel utilisateur
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    print(f"Utilisateur {email} ajouté avec succès")
    return redirect(url_for('admin.dashboard'))


# Route : Supprimer un utilisateur
@admin_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Utilisateur non trouvé'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': f'Utilisateur {user.email} supprimé avec succès'})


# Route : Lister les utilisateurs
@admin_bp.route('/list_users', methods=['GET'])
def list_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'email': user.email, 'role': user.role} for user in users]
    return jsonify({'users':users_list})
