import React from "react";
import { useNavigate } from "react-router-dom";

function NavBar() {

    const navigate = useNavigate();

    return (
        <div id = 'nav-bar'>

            <button onClick = { () => navigate("/Books") }>Books</button>

            <button onClick = { () => navigate("/Libraries") }>Libraries</button>

        </div>
    )
}

export default NavBar;