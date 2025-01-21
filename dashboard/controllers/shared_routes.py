from flask import Blueprint, redirect, render_template, request, jsonify, session, url_for
from models import Region, Espece, TableDescription
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
    regions = [region.nom_region for region in Region.query.distinct(Region.nom_region).all()]
    especes = [espece.nom_espece for espece in Espece.query.distinct(Espece.nom_espece).all()]
    current_user = User.query.filter_by(email=session['email']).first()
    return render_template('agent/prediction.html', current_user=current_user, regions=regions, especes=especes)

#Route : Formulaire de prédiction (POST)
@shared_bp.route('/predict', methods=['POST'])
def predict_route():
    user_data = request.json
    rendement_fcfa = predict(user_data, 500000)
    espece_nom = user_data.get('espece')
    
    espece = Espece.query.filter_by(nom_espece=espece_nom).first()
    rendement_tonnes = rendement_fcfa / espece.prix_tonne  
    
    return jsonify({'rendement_tonnes': rendement_tonnes, 'rendement_fcfa': rendement_fcfa})


# Route : Afficher les tables
@shared_bp.route('/tables', methods=['GET'])
def tables():
    current_user = User.query.filter_by(email=session['email']).first()
    tables_description = TableDescription.query.all()
    return render_template('agent/table.html', current_user=current_user, tables=tables_description)