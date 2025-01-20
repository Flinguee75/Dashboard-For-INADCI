from flask import Blueprint, session
from models.user_model import User
from permissions import role_required
from flask import render_template

agent_bp = Blueprint('agent', __name__)

@agent_bp.route('/dashboard')
def dashboard():
    current_user = User.query.filter_by(email=session['email']).first()
    return render_template('tableau_de_bord/index.html', current_user=current_user)
