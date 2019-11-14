import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";

class BeritaTerkini extends React.Component {
  render() {
    return (
      <table className="table-center berita-terkini">
        <tbody>
          <tr>
            <td className="text red">{this.props.title}</td>
          </tr>
          <tr>
            <td className="text">{this.props.content}</td>
          </tr>
        </tbody>
      </table>
    );
  }
}

export default BeritaTerkini;
