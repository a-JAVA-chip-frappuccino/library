import React, { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";

import Home from "./layout-components/Home";

import Libraries from "./content-components/Libraries";
import Library from "./content-components/Library";
import Books from "./content-components/Books";
import Book from "./content-components/Book";
import Libaries from "./content-components/Libraries";

function App() {

    const [libraries, setLibraries] = useState([])
    const [books, setBooks] = useState([])

    useEffect(() => {
        fetch("/libraries")
        .then((resp) => resp.json())
        .then((fetchedLibArr) => setLibraries(fetchedLibArr))
    }, [])

    useEffect(() => {
        fetch("/books")
        .then((resp) => resp.json())
        .then((fetchedBookArr) => setBooks(fetchedBookArr))
    }, [])

    return (
        <Routes>
            <Route path = '/' element = { <Home /> } />
                <Route path = '/libraries'>
                    <Route index element = { <Libraries libaries = { libraries } /> } />
                    <Route path = ':id' element = { <Library /> } />
                </Route>
                <Route path = '/books'>
                    <Route index element = { <Books books = { books } /> } />
                    <Route path = ':id' element = { <Book /> } />
                </Route>
        </Routes>
    )
}

export default App;