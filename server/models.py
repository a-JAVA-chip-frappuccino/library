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

    serialize_rules = ('-libraries.books', '-author.books_by_author', '-genre.books_with_genre')

    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    publication_year = db.Column(db.Integer)

    libraries_with_book = db.relationship('BookAtLibrary', backref = 'book')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    serialize_rules = ('-book.author_id')

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_of_birth = db.Column(db.String)

    books_by_author = db.relationship('Book', backref = 'author')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'

    serialize_rules = ('-books_with_genre')

    id = db.Column(db.Integer, primary_key = True)
    genre = db.Column(db.String)

    books_with_genre = db.relationship('Book', backref = 'genre')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Library(db.Model, SerializerMixin):
    __tablename__ = 'libraries'

    serialize_rules = ('-books.libraries_with_book')

    id = db.Column(db.Integer, primary_key = True)
    branch_name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)

    books_at_library = db.relationship('BookAtLibrary', backref = 'library')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class BookAtLibrary(db.Model, SerializerMixin):
    __tablename__ = 'book_at_library'

    id = db.Column(db.Integer, primary_key = True)

    book_isbn = db.Column(db.Integer, db.ForeignKey('books.isbn'))
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
