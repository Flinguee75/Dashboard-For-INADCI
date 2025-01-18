from models import db
class Region(db.Model):

    __tablename__ = "regions"
    id_region = db.Column(db.Integer, primary_key=True)
    nom_region = db.Column(db.String(100), nullable=False)

    # Relation avec les autres tables
    #meteorologie = db.relationship('Meteorologie', backref='region', lazy=True)
   # plantations = db.relationship('Plantation', backref='region', lazy=True)
    #statistiques = db.relationship('Statistique', backref='region', lazy=True)