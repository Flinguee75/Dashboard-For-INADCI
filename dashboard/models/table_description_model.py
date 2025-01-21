from models import db
class TableDescription(db.Model):
    __tablename__ = 'table_descriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    