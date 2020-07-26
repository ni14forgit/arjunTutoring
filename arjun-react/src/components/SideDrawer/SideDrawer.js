import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./SideDrawer.css";
import Switch from "@material-ui/core/Switch";

const SideDrawer = (props) => {
  let drawerClasses = "side-drawer";
  if (props.show) {
    drawerClasses = "side-drawer open";
  }
  return (
    <nav className={drawerClasses}>
      <div>
        <h1 id="header">My Family</h1>
        <ul>
          <li>
            <Link to="/weather" onClick={props.toggle}>
              <b>Weather</b>
            </Link>
          </li>
          <li>
            <Link to="/" onClick={props.toggle}>
              <b>Home</b>
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default SideDrawer;
