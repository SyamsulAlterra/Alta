import React from "react";
import { BrowserRouter as BR, Switch, Route, Redirect } from "react-router-dom";
import Page from "../page/page";
import Login from "../page/login";
import Tes from "../page/tes";
import Profil from "../page/profil";

function MyRoute(props) {
  return (
    <Switch>
      <Route exact path="/home" component={Page} />
      {/* <Route exact path="/:category" component={PageCategory} /> */}
      <Route exact path="/sepak_bola" component={Page} />
      <Route exact path="/hiburan" component={Page} />
      <Route exact path="/politik" component={Page} />
      <Route exact path="/ekonomi" component={Page} />
      <Route exact path="/" component={Login} />
      <Route exact path="/tes" component={Tes} />
      <Route exact path="/profil" component={Profil} />
    </Switch>
  );
}

export default MyRoute;
