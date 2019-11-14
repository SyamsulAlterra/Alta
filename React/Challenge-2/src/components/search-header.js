import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";

class SearchHeader extends React.Component {
  constructor(props) {
    super(props);
    this.onChange = this.onChange.bind(this);
  }

  onChange(e) {
    // e.preventDefault();
    const input = e.target.value;
    this.props.onChange(input);
  }

  render() {
    return (
      <table className="table-center search">
        <tbody>
          <tr>
            <td>
              {/* <SearchField
                placeholder="Search..."
                onChange={this.onChange}
                searchText="This is initial search text"
                classNames="test-class"
              /> */}
              <input
                type="search"
                placeholder="search"
                onChange={this.onChange}
              />
            </td>
            {/* <td>
              <img
                src="https://dumielauxepices.net/sites/default/files/search-icon-circle-755348-7781912.png"
                alt=""
              />
            </td> */}
          </tr>
        </tbody>
      </table>
    );
  }
}

export default SearchHeader;
