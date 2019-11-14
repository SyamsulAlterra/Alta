import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import Header from "../components/header";

class Profil extends React.Component {
  render() {
    return (
      <div class="">
        <Header />
        <h1>{localStorage.getItem("nama")}</h1>
        <h1>{localStorage.getItem("email")}</h1>
      </div>
    );
  }
}

export default Profil;
