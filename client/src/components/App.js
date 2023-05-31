import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./Layout";
import Home from "./Home";
import Header from "./Header";
import Footer from "./Footer";

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path = '/' element = { <Layout /> }>
                    <Route index element = { <Home /> } />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default App;