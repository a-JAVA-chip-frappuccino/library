import React from "react";

function Book( { isbn, title, author_id, genre_id, publication_year } ) {
    
    return (
        <li>
            <h2>{title}</h2>
            <h3>{author_id} TODO: REPLACE WITH DB GRAB</h3>
            <h3>{genre_id} TODO: REPLACE WITH DB GRAB</h3>
            <p>{publication_year}</p>
        </li>
    )
}

export default Book;