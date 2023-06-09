import React from "react";

function Library( { id, branch_name, city, state } ) {
    
    return (
        <li>
            <h2>{branch_name}</h2>
            <p>{city}, {state}</p>
        </li>
    )
}

export default Library;