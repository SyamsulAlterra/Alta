import React from "react";
import Header from "../components/header.js";
import Footer from "../components/footer.js";
import About from "../components/content-about.js";

class PageAbout extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <About />
        <Footer />
      </div>
    );
  }
}

export default PageAbout;
