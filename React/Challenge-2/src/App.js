import React from "react";
import logo from "./logo.svg";
import "./App.css";
import MyRoute from "./components/myRoute";
import { BrowserRouter as BR, Switch, Route } from "react-router-dom";

function App() {
  return (
    <BR>
      <MyRoute />
    </BR>
  );
}

export default App;
