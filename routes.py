from flask import render_template,url_for,request
from . import app,models

@app.route('/')

@app.route('/films')
def films():
    liste_films = models.Film.query.all()
    return render_template('tous_films.html', title='Nos films', lFilms = liste_films)
@app.route("/accueil")
def accueil():
    liste_genres = models.Film.query.with_entities(models.Film.genre_film).distinct().all()
    genre_unique = []
    for genre in liste_genres:
        genres=genre[0].split(',')
        if (len(genres)>1):
            for i in genres:
                if i.strip() not in genre_unique:
                    genre_unique.append(i.strip())




    return render_template('accueil.html',title='Bienvenue dans notre cinema',genres=genre_unique)
@app.route("/genres")
def genres():

    nom_genre = request.args.get('genre')

    liste_films = models.Film.query.filter(models.Film.genre_film.ilike('%'+nom_genre+'%')).all()

    return render_template('films_genre.html', title='Nos films '+ nom_genre, lFilms = liste_films,genre = nom_genre)
@app.route("/film")
def film():
    id_film = request.args.get('id')
    film = models.Film.query.filter_by(id_film=id_film).first()
    return render_template('film.html', title=film.titre_film, film = film)
@app.route("/rech")
def rech():
    nom_film = request.args.get('nom')
    liste_films = models.Film.query.filter(models.Film.titre_film.ilike('%'+nom_film+'%')).all()
    return render_template('recherche.html', title='Resultat de la recherche', lFilms = liste_films)