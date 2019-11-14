import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import Header from "../components/header";
import Content from "../components/content";
// import { BrowserRouter as BR, Switch, Route } from "react-router-dom";

const axios = require("axios");

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.hostNews = "https://newsapi.org/v2/everything?";
    this.query = "q=Indonesia&";
    this.apikey = "apikey=f36d39ed6dca46759870db4ee3c9e304";
    this.state = {
      news: [{ description: "description", title: "title" }],
      searchInput: ""
    };
  }

  componentDidMount() {
    let url = this.hostNews + this.query + this.apikey;
    if (this.state.searchInput == "") {
      axios.get(url).then(response => {
        this.setState({ news: response.data.articles });
      });
    } else {
      url = this.hostNews + "q=" + this.state.searchInput + "&" + this.apikey;
      axios.get(url).then(response => {
        this.setState({ news: response.data.articles });
      });
    }
  }

  onChange = keyword => {
    this.setState({ searchInput: keyword }, () => {
      let url = this.hostNews + this.query + this.apikey;
      if (this.state.searchInput == "") {
        axios.get(url).then(response => {
          this.setState({ news: response.data.articles });
        });
      } else {
        url = this.hostNews + "q=" + this.state.searchInput + "&" + this.apikey;
        axios.get(url).then(response => {
          this.setState({ news: response.data.articles });
        });
      }
    });
  };

  handleClick = category => {
    this.setState({ searchInput: category }, () => {
      let url =
        this.hostNews + "q=" + this.state.searchInput + "&" + this.apikey;
      axios.get(url).then(response => {
        this.setState({ news: response.data.articles });
      });
    });
  };

  render() {
    console.log(this.state.searchInput, "search input");
    return (
      <div>
        <Header onChange={this.onChange} onClick={this.handleClick} />
        <div className="blank" />
        <Content content={this.state.news} />
        <div className="blank" />
      </div>
    );
  }
}

export default Page;
