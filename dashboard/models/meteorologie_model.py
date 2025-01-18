from models import db
class Meteorologie(db.Model):

    __tablename__ = "meteorologie"

    id_meteo = db.Column(db.Integer, primary_key=True)
    pluviometrie = db.Column(db.Float, nullable=True)
    temperature_min = db.Column(db.Float, nullable=True)
    temperature_max = db.Column(db.Float, nullable=True)
    #id_region = db.Column(db.Integer, db.ForeignKey('regions.id_region'), nullable=False)
    date_meteo = db.Column(db.Date, nullable=True, unique=True)

    