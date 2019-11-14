import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import logo from "../logo.svg";

class LogoHeader extends React.Component {
  render() {
    return (
      <table>
        <tbody>
          <tr>
            <td>
              <img className="header-logo" src={logo} alt="" />
            </td>
            <td>KabarKabar</td>
          </tr>
        </tbody>
      </table>
    );
  }
}

export default LogoHeader;
