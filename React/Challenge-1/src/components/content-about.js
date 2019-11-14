import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import imgdot from "../img/img-dot.png";
import matthew from "../img/matthew-hamilton-tNCH0sKSZbA-unsplash.jpg";

class About extends React.Component {
  render() {
    return (
      <div>
        <div>
          <div class="container-fluid">
            <div class="row aboutme align-items-center">
              <div class="container">
                <div class="background2">
                  <h2>ABOUT ME.</h2>
                </div>
              </div>
            </div>
          </div>
          <div class="container">
            <div class="row SettingRow3">
              <div class="col-md-7">
                <div class="content-paragraph">
                  <p>
                    Hello! I’m Anne Sullivan, a full-stack engineer based in
                    Malang, IDN who enjoys building things that live on the
                    internet. I develop exceptional websites and web apps that
                    provide intuitive, pixel-perfect user interfaces with
                    efficient and modern backends.
                  </p>
                  <p>
                    Shortly after graduating from Alterra Academy, I joined the
                    engineering team at Alterra where I work on a wide variety
                    of interesting and meaningful projects on a daily basis.
                  </p>
                  <p>
                    Here’s few technologies I’ve been working with recently :
                  </p>
                </div>
                <table class="table table-bordered">
                  <tbody>
                    <tr>
                      <td>HTML & CSS</td>
                      <td>Serverless</td>
                      <td>Scrum</td>
                    </tr>
                    <tr>
                      <td>Programming</td>
                      <td>Restful API</td>
                      <td>Test-Driven Dev</td>
                    </tr>
                    <tr>
                      <td>Database</td>
                      <td>Javascript</td>
                      <td>Software Testing</td>
                    </tr>
                    <tr>
                      <td>Git & Github</td>
                      <td>Single Page App</td>
                      <td>UI/UX Designer</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="col-md-5">
                <div class="imagePicture">
                  <img
                    src={imgdot}
                    class="img-fluid image1"
                    alt="Responsive image"
                  />
                  <img
                    src={matthew}
                    class="img-fluid image2"
                    alt="Responsive image"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default About;
