from app import db
from sqlalchemy.orm import relationship

class Fruta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    tamaño = db.Column(db.String(255), nullable=False)
    tfrutha = db.Column(db.Integer(), db.ForeignKey('tfrutha.id'))