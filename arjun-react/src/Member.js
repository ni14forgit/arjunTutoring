import React, { useState } from "react";
import "./App.css";

const Member = (props) => {
  const [showMessage, setTrueFalseShowMessage] = useState(false);
  return (
    <div>
      <img src={props.image} width="30%"></img>
      <h1>{props.name}</h1>
      <p>{props.description}</p>
      <button onClick={() => setTrueFalseShowMessage(!showMessage)}>
        Click here to show an {props.embarrassingorfun} Secret about{" "}
        {props.name}
      </button>
      {showMessage ? (
        <p>
          <b>{props.secret}</b>
        </p>
      ) : null}
    </div>
  );
};

export default Member;
