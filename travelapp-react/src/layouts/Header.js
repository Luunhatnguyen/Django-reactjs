import { BrowserRouter, Link, Navigate } from "react-router-dom";
import React, { useState } from 'react';
import { Container, FormControl, Navbar, Nav, Button, Form } from "react-bootstrap";
import { useSelector, useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom";
import cookie from "react-cookies";
import { logoutUser } from "../ActionCreators/UserCreators"

// let path = <Link className="nav-link text-danger" to="/login"> LOGIN </Link>

export default function Header(){

    const user = useSelector(state => state.user.user)
    const dispatch = useDispatch()
    const [q, setQ] = useState("")

    const search = (event) => {
        event.preventDefault()
        Navigate(`/?q=${q}`)
    }

    const logout = (event) => {
        event.preventDefault()

        cookie.remove("access_token")
        cookie.remove("user")
        dispatch(logoutUser())
    }

    let path = <>
        <Link className="nav-link text-danger" to="/login">Dang nhap</Link>
        <Link className="nav-link text-danger" to="/register">Dang ky</Link>
    </>
    if (user !== null && user !== undefined) {
        path = <>
            <Link className="nav-link text-danger" to="/">{ user.username }</Link>
            <Link className="nav-link text-danger" onClick={logout}>Dang xuat</Link>
        </>
       

    }


    return(
        <Navbar>
            <Container>
                <Navbar.Brand bg="light" expand="lg">TravelApp</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link className="nav-link" to="/">Trang chủ</Link>
                        <Link className="nav-link" to="/tour">Tour</Link>
                        {path} 
                    </Nav>
                    <Form className="d-flex" onSubmit={search}>
                        <FormControl type="search" placeholder="Nhap tu khoa..."
                        className = "mr-2" aria-label="Search" value={q}
                        onChange={ (event) => setQ(event.target.value)} />
                        <Button type="submit" variant="outline-success">Tim kiem</Button>
                    </Form>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

