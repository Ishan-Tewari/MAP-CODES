from settings import *
import json

# initializing the database
db = SQLAlchemy(app)

# creating movie class corresponding to the movies table in our database
class Movie(db.Model):
    __tablename__ = 'movies' # giving the table a name

    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), nullable= False)
    year = db.Column(db.Integer, nullable= False)
    genre = db.Column(db.String(80), nullable= False)

    # function to display output as json
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'genre': self.genre
        }

    # function to add a movie to the database
    def add_movie(_title, _year, _genre):
        movie = Movie(title = _title,year = _year,genre = _genre)
        db.session.add(movie)
        db.session.commit()

    # function to return all the movies in the database
    def get_all_movies():
        return [Movie.json(movie) for movie in Movie.query.all()]

    # function to return the movie by id 
    def get_movie(_id):
        return [Movie.json(Movie.query.filter_by(id = _id).first())]

    # function to update the movie using id
    def update_movie(_id, _title, _year, _genre):
        movie_to_update = Movie.query.filter_by(id = _id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()
    
    # function to delete a movie from database
    def delete_movie(_id):
        Movie.query.filter_by(id = _id).delete()
        db.session.commit()