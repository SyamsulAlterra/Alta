import React from "react";
import Header from "../components/header.js";
import Footer from "../components/footer.js";
import Home from "../components/content-home.js";

class PageHome extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Home />
        <Footer />
      </div>
    );
  }
}

export default PageHome;
