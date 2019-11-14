import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import alta from "../img/logo-ALTA-v2.png";
import fb from "../img/ic_fb.png";
import twitter from "../img/ic-twitter.png";
import instagram from "../img/ic-instagram.png";
import linkedin from "../img/ic-linkedin.png";

class Footer extends React.Component {
  render() {
    return (
      <div>
        <footer>
          <div class="container-fluid">
            <div class="row">
              <div class="col-lg-6 col-md-4">
                <div class="footerImage">
                  <img src={alta} alt="" />
                </div>
              </div>
              <div class="col-lg-3 col-md-4">
                <div class="footerMedsos">
                  <div class="medsosFill">
                    <div class="container-fluid">
                      <div class="row">
                        <div class="col-md-12">
                          <div class="text">Social Media</div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-3-icon">
                          <div class="fbImage">
                            <img src={fb} alt="" />
                          </div>
                        </div>
                        <div class="col-md-3-icon">
                          <div class="twitterImage">
                            <img src={twitter} alt="" />
                          </div>
                        </div>
                        <div class="col-md-3-icon">
                          <div class="instImage">
                            <img src={instagram} alt="" />
                          </div>
                        </div>
                        <div class="col-md-3-icon">
                          <div class="linkedImage">
                            <img src={linkedin} alt="" />
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-4">
                <div class="footerCopyright">copyright @ 2019 Alterra</div>
              </div>
            </div>
          </div>
        </footer>
      </div>
    );
  }
}

export default Footer;
