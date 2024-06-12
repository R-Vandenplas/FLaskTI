from . import app, db
from flask_sqlalchemy import SQLAlchemy

class Film(db.Model):
    id_film = db.Column(db.Integer, primary_key=True)
    titre_film = db.Column(db.String(100), nullable=False)
    description_film = db.Column(db.String(1000), nullable=False)
    genre_film = db.Column(db.String(100), nullable=False)
    real_film = db.Column(db.String(100), nullable=False)
    duree_film = db.Column(db.Double, nullable=False)
    affiche_film = db.Column(db.String(100), nullable=False)
    date_sortie = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Film('{self.titre_film}', '{self.description_film}', '{self.genre_film}', '{self.real_film}', '{self.duree_film}', '{self.affiche_film}', '{self.date_sortie}')"