import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";

class Experience extends React.Component {
  render() {
    return (
      <div>
        <div className="pageTitle">
          <div className="container">
            <div className="row">
              <div className="col-md-12">
                <div className="text">Experience</div>
              </div>
            </div>
          </div>
        </div>
        <div class="blank1" />

        <div class="historyList">
          <div class="historyBox">
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-1">
                  <div class="garis" />
                  <div class="bungkusDot">
                    <div class="dot" />
                  </div>
                </div>

                <div class="col-md-11">
                  <div class="historyElement">
                    <div class="container-fluid">
                      <div class="row">
                        <div class="col-md-12">
                          <div class="titleDate">
                            <span class="title">
                              {" "}
                              FULL-STACK ENGINEER - ALTERRA ACADEMY{" "}
                            </span>{" "}
                            <br />
                            <span class="date"> May, 2019 - Present</span>
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-12">
                          <ul class="description">
                            <li>
                              - Write modern, performant, maintanable, code for
                              diverse array of client and internal projects
                            </li>
                            <li>
                              - Work with variety of different languages,
                              platforms, frameworks, and content management
                              system such as Javascript, TypeScript, Gatsby,
                              React, Craft, Wordpress, Prismic, and Netlify
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="historyBox">
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-1">
                  <div class="garis" />
                  <div class="bungkusDot">
                    <div class="dot" />
                  </div>
                </div>

                <div class="col-md-11">
                  <div class="bungkusElement">
                    <div class="historyElement">
                      <div class="container-fluid">
                        <div class="row">
                          <div class="col-md-12">
                            <div class="titleDate">
                              <span class="title">
                                {" "}
                                FRONTEND ENGINEER - APPLE{" "}
                              </span>{" "}
                              <br />
                              <span class="date"> May, 2018 - May, 2019</span>
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-md-12">
                            <ul class="description">
                              <li>
                                Developed and maintained code for in-house and
                                client websites primarily using HTML, CSS, Sass,
                                and JavaScript
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="historyBox">
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-1">
                  <div class="garis" />
                  <div class="bungkusDot">
                    <div class="dot" />
                  </div>
                </div>

                <div class="col-md-11">
                  <div class="historyElement">
                    <div class="container-fluid">
                      <div class="row">
                        <div class="col-md-12">
                          <div class="titleDate">
                            <span class="title">UI/UX DESIGN - SCOUT</span>{" "}
                            <br />
                            <span class="date">
                              {" "}
                              Januari, 2018 - April, 2018
                            </span>
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-12">
                          <ul class="description">
                            <li>
                              - Developed and shipped highly interactive web
                              applications for Apple Music using Ember.js
                            </li>
                            <li>
                              - Architected and implemented the front-end of
                              Apple Music's embeddable web player widget, which
                              let user log in and listen to full songs in the
                              browser
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="blank2" />
      </div>
    );
  }
}

export default Experience;
