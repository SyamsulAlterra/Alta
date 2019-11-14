import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import LogoHeader from "./logo-header";
import MasukDaftar from "./masuk-daftar";
import MenuHeader from "./menu-header";
import SearchHeader from "./search-header";

class Header extends React.Component {
  constructor(props) {
    super(props);
    // this.state = { inputSearch: "search here" };
    // this.onChange = this.onChange.bind(this);
  }

  onChange = input => {
    this.props.onChange(input);
    // this.setState({ inputSearch: keyword });
  };

  handleClick = input => {
    this.props.onClick(input);
  };

  render() {
    // console.log(this.state.inputSearch);
    return (
      <div className="container-fluid header-bg">
        <div className="row">
          <div className="col-2">
            <table className="height100">
              <tbody>
                <tr>
                  <td className="align-middle">
                    <LogoHeader />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div className="col-4">
            <table className="height100">
              <tbody>
                <tr>
                  <td className="align-middle">
                    <MenuHeader onClick={this.handleClick} />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div className="col-4">
            <table className="height100">
              <tbody>
                <tr>
                  <td className="align-middle">
                    <SearchHeader onChange={this.onChange} />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div className="col-2">
            <table className="height100">
              <tbody>
                <tr>
                  <td className="align-middle">
                    <MasukDaftar />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }
}

export default Header;
