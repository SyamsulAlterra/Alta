import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import { Link, Redirect, withRouter } from "react-router-dom";
// import "../js/jquery-3.3.1.slim.min.js";
// import "../js/bootstrap.min.js";

class MenuHeader extends React.Component {
  constructor(props) {
    super(props);
    this.state = { category: "", status: "" };
  }

  componentWillMount() {
    this.setState({ status: localStorage.getItem("status") });
  }

  sepakBola = () => {
    this.setState({ category: "football" }, () => {
      this.props.onClick(this.state.category);
      console.log(this.state.category);
    });
  };

  ekonomi = () => {
    this.setState({ category: "economy" }, () => {
      this.props.onClick(this.state.category);
      console.log(this.state.category);
    });
  };

  politik = () => {
    this.setState({ category: "politics" }, () => {
      this.props.onClick(this.state.category);
      console.log(this.state.category);
    });
  };

  hiburan = () => {
    this.setState({ category: "entertainment" }, () => {
      this.props.onClick(this.state.category);
      console.log(this.state.category);
    });
  };

  signup = () => {
    this.setState({ status: "false" }, () => {
      localStorage.setItem("status", "false");
      this.props.history.push("/");
    });
  };

  renderRedirect = () => {
    if (this.state.status === "false") {
      return <Redirect to="/" />;
    }
  };

  render() {
    // console.log(this.state.status);
    return (
      <div className="menu-header">
        {this.renderRedirect()}
        <table className="table-center">
          <tbody>
            <tr className="align-center">
              <td className="menu-item-list">
                <Link to="/sepak_bola" onClick={this.sepakBola}>
                  SepakBola
                </Link>
              </td>
              <td className="menu-item-list">
                <Link to="/ekonomi" onClick={this.ekonomi}>
                  Ekonomi
                </Link>
              </td>
              <td className="menu-item-list">
                <Link to="/politik" onClick={this.politik}>
                  Politik
                </Link>
              </td>
              <td className="menu-item-list">
                <Link to="/hiburan" onClick={this.hiburan}>
                  Hiburan
                </Link>
              </td>
              <td className="menu-item-list" onClick={this.signup}>
                Signup
              </td>
              <td className="menu-item-list">
                <Link to="/profil">Profil</Link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
}

// function Child({ match }) {
//   return (
//     <div>
//       <h3>ID: {match.params.id}</h3>
//     </div>
//   );
// }

// function ComponentWithRegex({ match }) {
//   return (
//     <div>
//       <h3>Only asc/desc are allowed: {match.params.direction}</h3>
//     </div>
//   );
// }

export default withRouter(MenuHeader);
