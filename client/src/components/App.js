import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Home";

function App() {

    console.log('here')
    return (
        <BrowserRouter>
            <Routes>
                <Route path = '/' element = {<Home />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App;