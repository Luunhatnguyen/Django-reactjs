import React from "react";
import { useState ,useEffect } from "react";
import classnames from "classnames";
import {NavbarBrand, Navbar, NavItem, NavLink, Container, Form, Nav } from "react-bootstrap";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import cookies from "react-cookies"
import { logoutUser } from "../ActionCreators/UserCreators";
import Api, { endpoints } from '../configs/Apis';

function IndexNavbar() {
    const [navbarColor, setNavbarColor] = React.useState("navbar-transparent");
    const [navbarCollapse, setNavbarCollapse] = React.useState(false);
    const user = useSelector(state => state.user.user)
    const dispatch = useDispatch()
    const [categories, setCategories] = useState([])
    
    useEffect(() => {
      let loadCategories = async () => {
          let res = await Api.get(endpoints['categories'])

          setCategories(res.data)
      }
      
      loadCategories()
      }, [])

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
            const logout = (event) => {
            event.preventDefault()

            cookies.remove('access_token')
            cookies.remove('user')
            dispatch(logoutUser())
        }

        let path = <>
            <Link className='nav-link text-success' to='/login'>Login</Link>
            <Link className='nav-link text-success' to='/register'>Register</Link>

        </>
        if (user !== null && user != undefined){ 
        
          path = <>
              <div className='user-img'>
                  <Link className='img-user' to='/'>
                      <img className='avt' src={'/static' + user.avatar} alt='avatar'/>{user.username}
                  </Link>
              </div>
              <Link className='nav-link text-success' to='#' onClick={logout}>Logout</Link>
          </>
      }
      return (
        <Navbar className={classnames("fixed-top", navbarColor)} expand="lg" >
          <Container>
            <div className="navbar-translate">
              <NavbarBrand
                href="#home"
              >
                TravelTour
              </NavbarBrand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav"></Navbar.Collapse>
            </div>


              <Nav className="me-auto">
                  <Link className="nav-link text-success" to="/">Trang chu</Link>
                  {categories.map(c => {
                    let path = `/?category_id=${c.id}`
                    return <Link className="nav-link text-success" to={path}>{c.name}</Link>
                  })
                  }
              </Nav>
              <NavItem>
                <NavLink  >
                 {path}
                </NavLink>
                </NavItem>
          </Container>
        </Navbar>
        
      );
    }
    
    export default IndexNavbar;