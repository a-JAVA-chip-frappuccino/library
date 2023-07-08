from flask import request, make_response, jsonify

from werkzeug.exceptions import NotFound

from config import app

from models import Book, Author, Genre, Library, BookAtLibrary

# server-side routes

@app.errorhandler(NotFound)
def route_not_found(e):
    response = make_response(
        "Oh, dear! The route you are looking for cannot be found!",
        404
    )
    
    return response

@app.route('/')
def home():
    return ""

@app.route('/books', methods = ['GET', 'POST'])
def books():
    
    if request.method == 'GET':
    
        books = Book.query.all()

        books_dict = [book.to_dict() for book in books]

        response = make_response(

            jsonify(books_dict),
            200
        )

    return response

@app.route('/authors', methods = ['GET', 'POST'])
def authors():
    
    if request.method == 'GET':

        authors = Author.query.all()

        authors_dict = [author.to_dict() for author in authors]

        response = make_response(
            jsonify(authors_dict),
            200
        )

    return response

@app.route('/libraries', methods = ['GET', 'POST'])
def libraries():

    if request.method == 'GET':

        libraries = Library.query.all()

        libraries_dict = [library.to_dict() for library in libraries]

        response = make_response(
            jsonify(libraries_dict),
            200
        )

    return response

@app.route('/genres', methods = ['GET'])
def genres():

    genres = Genre.query.all()

    genres_dict = [genre.to_dict() for genre in genres]

    response = make_response(
        jsonify(genres_dict),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port = 5555, debug = True)