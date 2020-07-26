import React, { useState } from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import InputBase from "@material-ui/core/InputBase";
import MenuIcon from "@material-ui/icons/Menu";
import { Link } from "react-router-dom";
import Search from "../SearchBar/SearchBar";
import NameContainer from "../SearchBar/NameContainer";
import "./NavBar.css";

const NavBar = (props) => {
  const { object, children } = props;

  const [searchTerm, setSearchTerm] = useState("");
  const [names, setNames] = useState([
    object[0].name,
    object[1].name,
    object[2].name,
    object[3].name,
  ]);

  const handleChange = (e) => {
    let h1;
    h1 = <h1>hi!</h1>;
    setSearchTerm(e.target.value);
  };

  const dynamicSearch = (e) => {
    return names.filter((name) =>
      name.toLowerCase().includes(this.state.searchTerm.toLowerCase())
    );
  };

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
          <div onChange={handleChange}>
            <Search value={searchTerm} />
          </div>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default NavBar;
