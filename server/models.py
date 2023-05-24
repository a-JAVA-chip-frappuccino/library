from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata = metadata)

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    publication_year = db.Column(db.Integer)

    libraries = db.relationship('BookAtLibrary', backref = 'book')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)

    books = db.relationship('Book', backref = 'author')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key = True)
    genre = db.Column(db.String)

    books = db.relationship('Book', backref = 'genre')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

class Library(db.Model, SerializerMixin):
    __tablename__ = 'libraries'

    id = db.Column(db.Integer, primary_key = True)
    branch_name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)

    books = db.relationship('BookAtLibrary', backref = 'library')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

class BookAtLibrary(db.Model, SerializerMixin):
    __tablename__ = 'book_at_library'

    id = db.Column(db.Integer, primary_key = True)

    book_isbn = db.Column(db.Integer, db.ForeignKey('books.isbn'))
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
