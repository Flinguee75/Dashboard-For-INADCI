from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAlchemy
db = SQLAlchemy()

from .user_model import User
from .espece_model import Espece
from .region_model import Region
from .meteorologie_model import Meteorologie
from .plantation_model import Plantation
from .statistique_model import Statistique