import Switch from "react-bootstrap/esm/Switch"
import { BrowserRouter as Router} from "react-router-dom";
import { BrowserRouter} from "react-router-dom";
import Headers from './Header';
import Footer from './Footer';
import Home from '../pages/Home';

export default function Body(){
    return(
        <>
            <Headers/>

            {/* <BrowserRouter>
                <h1>àkasdkfjas</h1>
                <Router>
                    <div className="App">
                        <Route path="/" exact component={Home} />
                    </div>
                </Router>
            </BrowserRouter> */}
                <h1>àkasdkfjas</h1>
                <Router>
                    <div className="App">
                        <Route path="/" exact component={Home} />
                    </div>
                </Router>

            <Footer/>
        </>
        
    )
}