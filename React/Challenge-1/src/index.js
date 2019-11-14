import React from "react";
import ReactDOM from "react-dom";
import "./css/index.css";

import PageHome from "./pages/home";
import PageAbout from "./pages/about";
import PageExperience from "./pages/experience";
import PageContact from "./pages/contact";

import * as serviceWorker from "./serviceWorker";

ReactDOM.render(<PageExperience />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
