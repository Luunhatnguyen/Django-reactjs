import { BrowserRouter, Link } from "react-router-dom";
import React from 'react';
import { Container, Navbar } from "react-bootstrap";

let path = <Link className="nav-link text-danger" to="/login"> LOGIN </Link>

export default function Header(){
    return(
        <Navbar>
            <Container>
                <Link to="/"> Home </Link>
                <Link to="/logout"> logout </Link>
                <Link to="/test"> test </Link>
                {path}
            </Container>
        </Navbar>
    )
}

