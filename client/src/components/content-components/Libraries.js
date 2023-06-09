import React from "react";

import Library from "./Library";

function Libaries( { libraries } ) {

    const mappedLibraries = libraries.map((library) => (
        <Library
            key = {library.id}
            id = {library.id}
            branch_name = {library.branch_name}
            city = {library.city}
            state = {library.state}
        />
    ))
    
    return (
        <ul>
            {mappedLibraries}
        </ul>
    )
}

export default Libaries;