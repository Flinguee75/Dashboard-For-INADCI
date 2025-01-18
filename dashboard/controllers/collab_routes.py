from flask import Blueprint, session, redirect, url_for, request

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Exemple de vérification avec une base de données simulée
    users = {
        "admin_user": {"password": "admin_pass", "role": "admin"},
        "agent_user": {"password": "agent_pass", "role": "agent"},
        "collab_user": {"password": "collab_pass", "role": "collaborateur"}
    }

    user = users.get(username)
    if user and user['password'] == password:
        session['user_id'] = username
        session['role'] = user['role']
        # Redirection basée sur le rôle
        if user['role'] == 'admin':
            return redirect(url_for('admin.admin_dashboard'))
        elif user['role'] == 'agent':
            return redirect(url_for('agent.agent_dashboard'))
        elif user['role'] == 'collaborateur':
            return redirect(url_for('user.collaborateur_dashboard'))
    return "Identifiants incorrects", 401

@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@user_bp.route('/collaborateur_dashboard')
def collaborateur_dashboard():
    if session.get('role') != 'collaborateur':
        return redirect(url_for('home'))
    return "<h1>Bienvenue dans le tableau de bord Collaborateur</h1>"