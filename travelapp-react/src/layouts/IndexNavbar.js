import React, { useState } from 'react';
import { Navigate } from 'react-router-dom';
import classnames from "classnames";
import {NavbarBrand, Navbar, NavItem, NavLink, Form } from "react-bootstrap";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import cookies from "react-cookies"
import { logoutUser } from "../ActionCreators/UserCreators";
import { Container, FormControl, Nav, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

function IndexNavbar() {
    const [navbarColor, setNavbarColor] = React.useState("navbar-transparent");
    const [navbarCollapse, setNavbarCollapse] = React.useState(false);
    const user = useSelector(state => state.user.user)
    const dispatch = useDispatch()
    const [q, setQ] = useState("")
    const toggleNavbarCollapse = () => {
      setNavbarCollapse(!navbarCollapse);
      document.documentElement.classList.toggle("nav-open");
    };
    React.useEffect(() => {
        const updateNavbarColor = () => {
          if (
            document.documentElement.scrollTop > 299 ||
            document.body.scrollTop > 299
          ) {
            setNavbarColor("");
          } else if (
            document.documentElement.scrollTop < 300 ||
            document.body.scrollTop < 300
          ) {
            setNavbarColor("navbar-transparent");
          }
        };
    
        window.addEventListener("scroll", updateNavbarColor);
    
        return function cleanup() {
          window.removeEventListener("scroll", updateNavbarColor);
        };
      });
          const search = (event) => {
            event.preventDefault()
            Navigate(`/?q=${q}`)
        }

        const logout = (event) => {
            event.preventDefault()
    
            cookies.remove("access_token")
            cookies.remove("user")
            dispatch(logoutUser())
        }
        let path = <>
        <Link className="nav-link text-success"  to="/login">Đăng nhập</Link>
        <Link className="nav-link text-success"  to="/register">Đăng kí</Link>
        </>
        if (user !== null && user !== undefined) {
        path = <>
            <Link className="nav-link text-success "  to="/">{user.username}</Link>
            <Link className="nav-link text-success"  onClick={logout}>Đăng xuất</Link>
            </>
    }
      return (
        // <Navbar className={classnames("fixed-top", navbarColor)} expand="lg" >
        //   <Container>
        //     <div className="navbar-translate">
        //       <NavbarBrand
        //         data-placement="bottom"
        //         href="/index"
        //         target="_blank"
        //         title="Coded by Creative Tim"
        //       >
        //         Travel Tour
        //       </NavbarBrand>
            
        //     </div>
            
        //         <NavItem >
        //           <NavLink
        //             href="https://demos.creative-tim.com/paper-kit-react/#/documentation?ref=pkr-index-navbar"
        //             target="_blank"
        //             className="text-success" 
        //           >
        //              Documentation
        //           </NavLink>
        //         </NavItem>
        //     <NavItem>
        //           <NavLink
        //             href="https://demos.creative-tim.com/paper-kit-react/#/documentation?ref=pkr-index-navbar"
        //             target="_blank"
        //             className="text-success" 
        //           >
        //             Documentation
        //           </NavLink>
        //     </NavItem>
        //     <NavItem > 
        //         <NavLink 
        //           >
        //           {path}
        //         </NavLink>
               
        //     </NavItem>
        //   </Container>
        // </Navbar>
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
      );
    }
    
    export default IndexNavbar;