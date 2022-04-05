import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './layouts/Header';
import Home from './component/Home';
import Body from './layouts/Body';
import Login from './component/Login';
import Footer from './layouts/Footer';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
          <Route path="/logout" element={<Home />} />
          <Route path='/login' element={<Login/>} />
      </Routes>
      <Body/>
      <Footer/>
    </BrowserRouter>
  );
}

export default App;
