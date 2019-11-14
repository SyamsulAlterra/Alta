import React from "react";
import "../css/style.css";
import logo from "../img/matthew-hamilton-tNCH0sKSZbA-unsplash.jpg";
import "../css/bootstrap.min.css";

class Home extends React.Component {
  render() {
    return (
      <div class="container">
        <div class="row">
          <div class="col-md-5">
            <div class="profile-pic">
              <img src={logo} alt="" />
            </div>
          </div>
          <div class="col-md-7">
            <div class="introduce">
              <h5>Hi, my name is</h5>
              <h1>Anne Sulivan</h1>
              <h3>I build things for the web</h3>
              <br />
              <div>
                <button type="button" class="btn btn-get btn-rounded">
                  <a class="get-in-touch" href="about.html">
                    Get In Touch
                  </a>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
