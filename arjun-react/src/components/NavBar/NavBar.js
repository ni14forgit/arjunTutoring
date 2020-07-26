import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import InputBase from "@material-ui/core/InputBase";
import MenuIcon from "@material-ui/icons/Menu";
import { Link } from "react-router-dom";
import Search from "../SearchBar/SearchBar";
import "./NavBar.css";

const NavBar = (props) => {
  return (
    <div className="root toolbar">
      <AppBar position="static">
        <Toolbar className="toolbar__navigation">
          {/* Hamburger Icon */}
          <div>
            <IconButton
              edge="start"
              className="menuButton"
              color="inherit"
              aria-label="menu"
              onClick={props.toggle}
            >
              <MenuIcon />
            </IconButton>
          </div>

          {/* Logo */}
          <Typography variant="h6" className="title toolbar__logo">
            <Link to="/">
              <b>My Family</b>
            </Link>
          </Typography>

          <Search object={props.object} />
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default NavBar;
