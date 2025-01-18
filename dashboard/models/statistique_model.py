from models import db
class Statistique(db.Model):


    __tablename__ = "statistiques"
    id_stat = db.Column(db.Integer, primary_key=True)
    #id_region = db.Column(db.Integer, db.ForeignKey('regions.id_region'), nullable=False)
    #id_espece = db.Column(db.Integer, db.ForeignKey('especes.id_espece'), nullable=False)
    #id_meteo = db.Column(db.Integer, db.ForeignKey('meteorologie.id_meteo'), nullable=True)
    taux_survie_plants = db.Column(db.Float, nullable=True)
    rendement_moyen = db.Column(db.Float, nullable=True)
    annee = db.Column(db.Integer, nullable=False)
