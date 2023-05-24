from app import app
from models import db, Book, Author, Genre, Library, BookAtLibrary

if __name__ == 'main':
    with app.app_context():

        # clear tables of current data
        print("Clearing all tables...")

        Book.query.delete()
        Author.query.delete()
        Genre.query.delete()
        Library.query.delete()
        BookAtLibrary.query.delete()

        # seed books table
        print("Seeding books table...")

        seed_books = [
            Book (
                isbn = '9780451528827',
                title = 'Anne of Green Gables',
                author_id = 1,
                genre_id = 5,
                publication_year = 1908
            ),
            Book (
                isbn = '9781421565989',
                title = 'Battle Royale',
                author_id = 3,
                genre_id = 2,
                publication_year = 1999
            ),
            Book (
                isbn = '1594484465',
                title = 'The Little Stranger',
                author_id = 5,
                genre_id = 3,
                publication_year = 2009
            ),
            Book (
                isbn = '1029779381',
                title = 'Bad Blood: Secrets and Lies in a Silicon Valley Startup',
                author_id = 4,
                genre_id = 9,
                publication_year = 2018
            ),
            Book (
                isbn = '0142437239',
                title = 'Don Quixote',
                author_id = 2,
                genre_id = 15,
                publication_year = 1615
            )
        ]

        # seed authors table
        print("Seeding authors table...")

        seed_authors = [
            Author (
                id = 1,
                first_name = 'Lucy Maud',
                last_name = 'Montgomery',
                date_of_birth = 1874-11-30
            ),
            Author (
                id = 2,
                first_name = 'Miguel',
                last_name = 'de Cervantes Saavedra',
                date_of_birth = 1547-09-29
            ),
            Author (
                id = 3,
                first_name = 'Koushun',
                last_name = 'Takami',
                date_of_birth = 1969-01-10
            ),
            Author (
                id = 4,
                first_name = 'John',
                last_name = 'Carreyrou',
                date_of_birth = None
            ),
            Author (
                id = 5,
                first_name = 'Sarah',
                last_name = 'Waters',
                date_of_birth = 1966-07-21
            )
        ]

        # seed genres table
        print("Seeding genres table...")

        seed_genres = [
            Genre (
                id = 1,
                genre = 'romance'
            ),
            Genre (
                id = 2,
                genre = 'action'
            ),
            Genre (
                id = 3,
                genre = 'horror'
            ),
            Genre (
                id = 4,
                genre = 'science fiction'
            ),
            Genre (
                id = 5,
                genre = 'slice of life'
            ),
            Genre (
                id = 6,
                genre = 'thriller'
            ),
            Genre (
                id = 7,
                genre = 'mystery'
            ),
            Genre (
                id = 8,
                genre = 'historical fiction'
            ),
            Genre (
                id = 9,
                genre = 'nonfiction'
            ),
            Genre (
                id = 10,
                genre = 'biography'
            ),
            Genre (
                id = 11,
                genre = 'autobiography'
            ),
            Genre (
                id = 12,
                genre = 'memoir'
            ),
            Genre (
                id = 13,
                genre = 'fantasy'
            ),
            Genre (
                id = 14,
                genre = 'comedy'
            ),
            Genre (
                id = 15,
                genre = 'parody and satire'
            )
        ]

        # seed libraries table
        print("Seeding libraries table...")

        seed_libraries = [
            Library (
                id = 1,
                branch_name = 'Boston Public Library',
                city = 'Boston',
                state = 'MA'
            ),
            Library (
                id = 2,
                branch_name = 'Harvard Library',
                city = 'Cambridge',
                state = 'MA'
            ),
            Library (
                id = 3,
                branch_name = 'Cornell University Library',
                city = 'Ithaca',
                state = 'NY'
            ),
            Library (
                id = 4,
                branch_name = 'Brandeis Library',
                city = 'Waltham',
                state = 'MA'
            )
        ]

        # seed book_at_library table

        print("Seeding book_at_library table...")

        seed_book_at_library = [
           BookAtLibrary (
                id = 1,
                book_isbn = '1594484465',
                library_id = 4
           ),
           BookAtLibrary (
                id = 2,
                book_isbn = '9780451528827',
                library_id = 1
           ),
           BookAtLibrary (
                id = 3,
                book_isbn = '9780451528827',
                library_id = 2
           ),
           BookAtLibrary (
               id = 4,
               book_isbn = '9781421565989',
               library_id = 2
           ),
           BookAtLibrary (
               id = 5,
               book_isbn = '1594484465',
               library_id = 3
           ),
           BookAtLibrary (
               id = 6,
               book_isbn = '1029779381',
               library_id = 2
           ),
           BookAtLibrary (
               id = 7,
               book_isbn = '1029779381',
               library_id = 3
           ),
           BookAtLibrary (
               id = 8,
               book_isbn = '0142437239',
               library_id = 1
           )
        ]