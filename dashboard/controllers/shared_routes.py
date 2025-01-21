from flask import Blueprint, redirect, render_template, request, jsonify, session, url_for
from models import TableDescription
from models import db
from models import User
from werkzeug.security import generate_password_hash
from prediction import predict
shared_bp = Blueprint('shared', __name__)

# Route : Tableau de bord de l'administrateur
@shared_bp.route('/dashboard', methods=['GET'])
def dashboard():
    current_user = User.query.filter_by(email=session['email']).first()
    return render_template('tableau_de_bord/index.html', current_user=current_user)

# Route : Prédiction

@shared_bp.route('/prediction', methods=['GET'])
def prediction():
    current_user = User.query.filter_by(email=session['email']).first()
    return render_template('agent/prediction.html', current_user=current_user)
    # Route : Formulaire de prédiction (POST)
@shared_bp.route('/prediction', methods=['POST'])
def prediction_post():
    current_user = User.query.filter_by(email=session['email']).first()
    
    user_data = {
        'nom_region': request.form.get('region'),
        'nom_espece': request.form.get('espece'),
        'superficie': float(request.form.get('superficie', 0)),
        'pluviometrie': float(request.form.get('pluviometrie', 0)),
        'temperature_moyenne': float(request.form.get('temperatureMoyenne', 0)),
        'mois_plantation': int(request.form.get('mois_plantation', 0))
    }
    
    prix = predict(user_data, 100000)
    
    return render_template('agent/prediction.html', current_user=current_user, prix=prix)

# Route : Afficher les tables
@shared_bp.route('/tables', methods=['GET'])
def tables():
    current_user = User.query.filter_by(email=session['email']).first()
    tables_description = TableDescription.query.all()
    return render_template('agent/table.html', current_user=current_user, tables=tables_description)