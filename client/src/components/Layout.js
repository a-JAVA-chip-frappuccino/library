import React from "react";
import { Outlet, Link } from "react-router-dom";

import Header from "./Header";
import Footer from "./Footer";

function Layout() {

    return (
        <>
            <Header />
            <nav>
                <ul>
                    <li>
                        <Link to = '/'>Home</Link>
                    </li>
                </ul>
            </nav>
            <Footer />
        </>
    )
}

export default Layout;