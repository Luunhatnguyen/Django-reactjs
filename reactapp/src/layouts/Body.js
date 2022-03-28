import Switch from "react-bootstrap/esm/Switch"
import { BrowserRouter, Route } from 'react-router-dom';
import Headers from './Header';
import Footer from './Footer';
import Home from '../pages/Home';

export default function Body(){
    return(
        <>
            <Headers/>
            <BrowserRouter>
                <Switch>
                    <Route exact path="/" component={Home}/>
                </Switch>
            </BrowserRouter>
            <Footer/>
        </>
    )
}