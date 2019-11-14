import React from "react";
import "../css/style.css";
import logo from "../img/logo-ALTA.png";
import "../css/bootstrap.min.css";

class Header extends React.Component {
  render() {
    return (
      <div>
        <div className="header">
          <div className="container">
            <div className="row">
              <div className="col-md-3">
                <div className="alterraImage">
                  <a href="home.html">
                    <img src={logo} alt="" />
                  </a>
                </div>
              </div>
              <div className="col-md-9">
                <div className="menu">
                  <ul className="topMenu">
                    <li>
                      <a href="home.html">Home</a>
                    </li>
                    <li>
                      <a href="about.html">About</a>
                    </li>
                    <li className="currentPage">
                      <a href="page-experience.html">Experience</a>
                    </li>
                    <li>
                      <a href="contact.html">Contact</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Header;
