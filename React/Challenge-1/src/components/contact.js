import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import altav2 from "../img/logo-ALTA-v2.png";

class Contact extends React.Component {
  render() {
    return (
      <div>
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-5">
              <div class="background-image">
                <div class="box-color">
                  <div class="logo">
                    <a href="home.html">
                      <img src={altav2} alt="" />
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-7">
              <div class="contact">
                <h3>Contact Us</h3>
                <br />
                <form action="" method="post">
                  <div>
                    <label for="fullname">
                      Full Name<span class="asterisk">*</span>
                    </label>
                    <br />
                    <input
                      class="form-layout"
                      type="text"
                      name="fullname"
                      id="fullname"
                      placeholder="Your Full Name"
                      required
                    />
                  </div>

                  <div>
                    <label for="email">
                      Email Address<span class="asterisk">*</span>
                    </label>
                    <br />
                    <input
                      class="form-layout"
                      type="text"
                      name="email"
                      id="email"
                      placeholder="example@domail.com"
                      required
                    />
                  </div>

                  <div>
                    <label for="phone">
                      Phone Number<span class="asterisk">*</span>
                    </label>
                    <br />
                    <input
                      class="form-layout"
                      type="text"
                      name="phone"
                      id="phone"
                      placeholder="08543890****"
                      required
                    />
                  </div>

                  <div>
                    <label for="nationality">Nationality</label>
                    <br />
                    <select
                      class="nationality-layout"
                      name="nationality"
                      id="nationality"
                    >
                      <option>Selected ...</option>
                      <option value="Indonesian">Indonesian</option>
                      <option value="Singaporean">Singaporean</option>
                      <option value="Malaysian">Malaysian</option>
                      <option value="Australian">Australian</option>
                    </select>
                  </div>
                  <div>
                    <label for="message">Message</label>
                    <br />
                    <input
                      class="message-layout"
                      type="text"
                      name="message"
                      id="message"
                    />
                    <br />
                    <br />
                  </div>
                  <div>
                    <button type="button" class="btn btn-submit btn-rounded">
                      {" "}
                      <a href="contact.html">Submit</a>
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Contact;
