import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./layout-components/Layout";
import Libraries from "./content-components/Libraries";
import Library from "./content-components/Library";
import Books from "./content-components/Books";

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path = '/' element = { <Layout /> } />
                <Route path = '/libraries'>
                    <Route index element = { <Libraries /> } />
                    <Route path = ':id' element = { <Library /> } />
                </Route>
                <Route path = '/books' element = { <Books /> } />
            </Routes>
        </BrowserRouter>
    )
}

export default App;