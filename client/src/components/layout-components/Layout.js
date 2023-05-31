import React from "react";
import { Outlet, Link } from "react-router-dom";

import Home from "./Home";
import Header from "./Header";
import Footer from "./Footer";

function Layout() {

    return (
        <>
            <Header />
            <Home />
            <Footer />
        </>
    )
}

export default Layout;