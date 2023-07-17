import React from "react";

function Book( { isbn, title, author_name, genre, publication_year } ) {
    
    return (
        <li>
            <h2>{title}</h2>
            <h3>{author_name}</h3>
            <h3>{genre}</h3>
            <p>{publication_year}</p>
        </li>
    )
}

export default Book;