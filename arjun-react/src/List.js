import React from "react";

const List = (props) => {
  return (
    <div>
      <p>
        Hi! I'm Arjun. I play {props.basketball}, {props.football} and{" "}
        {props.guitar}.
      </p>
      <p>I also like tennis and making movies.</p>
    </div>
  );
};

export default List;
