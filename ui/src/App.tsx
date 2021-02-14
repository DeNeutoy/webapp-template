
import React from 'react';
import { BrowserRouter, Route} from 'react-router-dom';


const Home = () => {
    return (
        <p>
            Hello, this is the most basic starter app.
        </p>
    )
}

const App = () => {
    return (
        <>
            <BrowserRouter>
                <Route path="/" exact component={Home}/>
            </BrowserRouter>
        </>
        )
    };


export default App;
