import React, { useState } from "react";
import Button from "@material-ui/core/Button";

const Member = (props) => {
  const [showMessage, setTrueFalseShowMessage] = useState(false);

  const style = { margin: "2vh", width: "47vw" };

  return (
    <div style={style}>
      <img
        style={{ width: "25vw", height: "40vh" }}
        src={props.image}
        height="100%"
        width="100%"
      ></img>
      <h1>{props.name}</h1>
      <p>{props.description}</p>
      <Button
        onClick={() => setTrueFalseShowMessage(!showMessage)}
        variant="contained"
        color="primary"
        style={{ zIndex: "0" }}
      >
        Click here to {showMessage ? "hide" : "show"} a{props.nornot}{" "}
        {props.embarrassingorfun} Secret about {props.name}
      </Button>
      {showMessage ? (
        <p>
          <b>{props.secret}</b>
        </p>
      ) : null}
    </div>
  );
};

export default Member;
