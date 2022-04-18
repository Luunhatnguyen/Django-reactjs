import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './layouts/Header';
import Home from './component/Home';
import Body from './layouts/Body';
import Login from './component/Login';
import Footer from './layouts/Footer';
import { Container } from 'react-bootstrap';

function App() {
  return (
    <Body></Body>
  );
}

export default App;
