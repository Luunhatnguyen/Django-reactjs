import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Footer from './Footer';
import Home from '../component/Home';
import Login from '../component/Login';
import Header from './Header';
import Footer_HotTour from './Footer_HotTour';
import Tour from '../component/Tour';
import Body_Info from './Body_Info';
import Services from './Service';
import IndexHeader from './IndexHeader';
import IndexNavbar from './IndexNavbar';
import ScrollToTop from './ScrollToTop';
import Register from '../component/Register';

export default function Body(){
    return(

        <BrowserRouter>
            {/* <Header /> */}
            <IndexNavbar />
            <IndexHeader />
            <Routes>
                <Route exact path="/" element={<Home/>} />
                <Route exact path="/login" element={<Login/>} />
                <Route exact path="/register" element={<Register/>} />
                <Route exact path="/tour" element={<Tour/>} />
            </Routes>
            <Footer_HotTour />
            <h1>DANH MUC CAC TOUR</h1>
            <Body_Info />
            <Services />
            <Footer />
            <ScrollToTop />
        </BrowserRouter>
    )
}