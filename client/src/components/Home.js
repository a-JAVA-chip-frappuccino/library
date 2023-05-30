import React, { useEffect, useState } from "react";

function Home() {

    useEffect(() => {
        fetch("http://127.0.0.1:5555/libraries")
            .then((resp) => resp.json())
            .then((libraries) => console.log(libraries))
    }, [])

    return (
        <div>wa</div>
    )
}

export default Home;