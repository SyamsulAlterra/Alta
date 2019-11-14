import React from "react";
import "../css/style.css";
import "../css/bootstrap.min.css";
import BeritaTerkiniBar from "./berita-terkini-bar";
import BeritaTerkini from "./berita-terkini";
import Headline from "./headline";

class Content extends React.Component {
  render() {
    // console.log(this.props.content[0]);
    console.log(this.props.content);
    let headlineNews = [];
    let a = [];
    if (this.props.content.length > 0) {
      headlineNews = this.props.content[0];
      a = this.props.content.slice(1, 4);
    }

    return (
      <div className="container">
        <div className="row">
          <div className="col-4">
            <BeritaTerkiniBar />
            {a.map(content => {
              return (
                <BeritaTerkini
                  content={content.content}
                  title={content.title}
                />
              );
            })}
          </div>
          <div className="col-8">
            <Headline headlineNews={headlineNews} />
          </div>
        </div>
      </div>
    );
  }
}

export default Content;
