import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";

class BeritaTerkiniBar extends React.Component {
  render() {
    return (
      <table className="table-center berita-terkini-bar">
        <tbody>
          <tr>
            <td className="align-left width">Berita Terkini</td>
            <td className="align-right">
              <a href="">lihat semua</a>
            </td>
          </tr>
        </tbody>
      </table>
    );
  }
}

export default BeritaTerkiniBar;
