import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";

class Tes extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: "", password: "", status: false };
  }

  handleSubmit = () => {
    this.setState({ status: !this.state.status });
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
    // console.log(this.state.status);
    return (
      <div class="login-box">
        {/* <form action=""> */}
        <label for="username">Username:</label> <br />
        <input
          type="text"
          name="username"
          placeholder="mau kemana"
          id="username"
          onChange={this.handleUsername}
        />
        <br />
        <label for="password">Password:</label> <br />
        <input
          type="text"
          name="password"
          id="password"
          placeholder="hayo"
          onChange={this.handlePassword}
        />
        <br />
        <button onClick={this.handleSubmit}>submit</button>
        {/* </form> */}
      </div>
    );
  }
}

export default Tes;
