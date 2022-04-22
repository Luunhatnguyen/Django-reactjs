import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Footer from './layouts/Footer';
import React,  { useReducer, createContext } from 'react';
import UserReducer from './reducers/UserReducer'
import IndexHeader from './layouts/IndexHeader'
import IndexNavbar from './layouts/IndexNavbar'
import ScrollToTop from './layouts/ScrollToTop'
import Header from './layouts/Header'
import Home from './component/Home';
import Login from './component/Login';
import Footer_HotTour from './layouts/Footer_HotTour';
import Body_Info from './layouts/Body_Info';
import Services from './layouts/Service';
import Register from './component/Register';

export const userContext = createContext()
const App = () => {
  const [user, dispatch] = useReducer(UserReducer)

  return (
    <BrowserRouter>
      <userContext.Provider value={[user, dispatch]}>
        <IndexNavbar />
        <IndexHeader />
        
        <Routes>
          <Route exact path="/" element={<Home/>} />
          <Route exact path="/login" element={<Login/>} />
          <Route exact path="/register" element={<Register/>} />
          {/* <Route exact path="/tour" element={<Tour/>} /> */}
        </Routes>
        <Footer_HotTour />
        <h1>DANH MUC CAC TOUR</h1>
        <Body_Info />
        <Header></Header>
        <Services />
        <Footer />
        <ScrollToTop />
      </userContext.Provider>
    </BrowserRouter>
  )
}

export default App
