from models import db
class Plantation(db.Model):

    __tablename__ = "plantations"

    id_plantation = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    superficie = db.Column(db.Float, nullable=False)
    #id_espece = db.Column(db.Integer, db.ForeignKey('especes.id_espece'), nullable=False)
    #id_region = db.Column(db.Integer, db.ForeignKey('regions.id_region'), nullable=False)

    # Relation avec les statistiques (si nécessaire)
    #tatistiques = db.relationship('Statistique', backref='plantation', lazy=True)