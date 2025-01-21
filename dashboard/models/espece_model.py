from models import db

class Espece(db.Model):
    __tablename__ = "especes" 

    id_espece = db.Column(db.Integer, primary_key=True)
    nom_espece = db.Column(db.String(100), nullable=False)
    type_espece = db.Column(db.String(50), nullable=True)
    prix_tonnes = db.Column(db.Float, nullable=False)
    