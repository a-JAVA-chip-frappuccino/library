import React from "react";

import Book from "./Book";

function Books( { books } ) {

    const mappedBooks = books.map((book) => (
        <Book
            key = {book.isbn}
            isbn = {book.isbn}
            title = {book.title}
            author_id = {book.author_id}
            genre_id = {book.genre_id}
            publication_year = {book.publication_year}
        />
    ))
    
    return (
        <ul>
            {mappedBooks}
        </ul>
    )
}

export default Books;