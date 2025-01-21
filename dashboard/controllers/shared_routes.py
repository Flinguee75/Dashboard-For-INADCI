from flask import Blueprint, redirect, render_template, request, jsonify, session, url_for
from models import TableDescription
from models import db
from models import User
from werkzeug.security import generate_password_hash

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

# Route : Afficher les tables
@shared_bp.route('/tables', methods=['GET'])
def tables():
    current_user = User.query.filter_by(email=session['email']).first()
    tables_description = TableDescription.query.all()
    return render_template('agent/table.html', current_user=current_user, tables=tables_description)