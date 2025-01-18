from functools import wraps
from flask import session, redirect, url_for

def role_required(required_role):
    """
    Décorateur pour vérifier si l'utilisateur connecté a le rôle requis.
    Redirige l'utilisateur vers la page d'accueil s'il n'a pas le bon rôle.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = session.get('role')
            if user_role != required_role:
                return redirect(url_for('home'))  # Redirige vers l'accueil
            return f(*args, **kwargs)
        return decorated_function
    return decorator