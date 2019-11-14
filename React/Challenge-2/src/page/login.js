import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import { Link, Redirect, Route, withRouter } from "react-router-dom";
import Header from "../components/header";
const axios = require("axios");

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: "", password: "", status: "" };
  }

  componentWillMount() {
    this.setState({ status: localStorage.getItem("status") });
    this.renderRedirect();
  }

  handleLogin = () => {
    let url = "https://syamsul5-react.free.beeceptor.com/login";
    this.setState({ status: "true" }, () => {
      axios.post(url).then(response => {
        localStorage.setItem("nama", response.data.nama);
        localStorage.setItem("email", response.data.email);
        localStorage.setItem("status", response.data.status);
        this.props.history.push("/home");
      });
    });
  };

  renderRedirect = () => {
    if (this.state.status === "true") {
      return <Redirect to="/home" />;
    }
  };

  handlePassword = e => {
    const pass = e.target.value;
    this.setState({ password: pass });
  };

  handleUsername = e => {
    const user = e.target.value;
    this.setState({ password: user });
  };

  render() {
    // console.log(this.state.username);
    // console.log(this.state.password);
    console.log(this.state.status);
    return (
      <div class="login">
        {/* {this.renderRedirect()} */}
        <Header />
        {/* <form action=""> */}
        <label for="username">Username:</label> <br />
        <input
          type="text"
          name="username"
          id="username"
          onChange={this.handleUsername}
        />
        <br />
        <label for="password">Password:</label> <br />
        <input
          type="text"
          name="password"
          id="password"
          onChange={this.handlePassword}
        />
        <br />
        <button onClick={this.handleLogin}>submit</button>
      </div>
    );
  }
}

export default withRouter(Login);
