from models import db

class Espece(db.Model):
    __tablename__ = "Espece" 

    id_espece = db.Column(db.Integer, primary_key=True)
    nom_espece = db.Column(db.String(100), nullable=False)
    type_espece = db.Column(db.String(50), nullable=True)

    # Relation avec les plantations
    #plantations = db.relationship('Plantation', backref='espece', lazy=True)
    #statistiques = db.relationship('Statistique', backref='espece', lazy=True)