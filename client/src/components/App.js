import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";

import Home from "./layout-components/Home";

import Libraries from "./content-components/Libraries";
import Library from "./content-components/Library";
import Books from "./content-components/Books";
import Book from "./content-components/Book";

function App() {

    return (
        <Routes>
            <Route path = '/' element = { <Home /> } />
                <Route path = '/libraries'>
                    <Route index element = { <Libraries /> } />
                    <Route path = ':id' element = { <Library /> } />
                </Route>
                <Route path = '/books'>
                    <Route index element = { <Books /> } />
                    <Route path = ':id' element = { <Book /> } />
                </Route>
        </Routes>
    )
}

export default App;