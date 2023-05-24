from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

from models import db, Book, Author, Genre, Library, BookAtLibrary

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# server-side routes

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

if __name__ == '__main__':
    app.run(port = 5555, debug = True)