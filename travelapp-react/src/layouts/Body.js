import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import Login from '../pages/Login';
import Register from '../pages/Register';
import Header from '../layouts/Header';
import IndexHeader from '../layouts/IndexHeader';
import Footer_HotTour from '../layouts/Footer_HotTour';
import Service from '../layouts/Service';
import Footer from '../layouts/Footer';
import ScrollToTop from '../layouts/ScrollToTop';
import Body_Info from './Body_Info';
import IndexNavbar from './IndexNavbar';


export default function Body() {
    return (
            <BrowserRouter>
                {/* <Header /> */}
                <IndexNavbar/>
                <IndexHeader />
                <Routes>
                    {/* <Route path ='/' element ={<Home />} />  */}
                    <Route  path ='/login' element ={<Login />} />
                    <Route  path ='/register' element ={<Register />} />
                </Routes> 
                <Footer_HotTour />
                <h1>DANH MUC CAC TOUR</h1>
                <Body_Info />
                <Service />
                <Footer />
                <ScrollToTop />
            </BrowserRouter>
       
    )
}