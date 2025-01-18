from flask import Blueprint
from permissions import role_required

agent_bp = Blueprint('agent', __name__)

@agent_bp.route('/agent_dashboard')
@role_required('agent')
def agent_dashboard():
    return "<h1>Bienvenue dans le tableau de bord Agent</h1>"