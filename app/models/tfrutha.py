from app import db

class Tfrutha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombret = db.Column(db.String(255), nullable=False)