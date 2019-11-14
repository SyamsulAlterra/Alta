import React from "react";
import Header from "../components/header.js";
import Footer from "../components/footer.js";
import Experience from "../components/content-experience.js";

class PageExperience extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Experience />
        <Footer />
      </div>
    );
  }
}

export default PageExperience;
