import React from "react";
import Name from "./Name";

const NameContainer = ({ names }) => {
  return (
    <div>
      {names.map((name) => {
        return (
          <div>
            <Name name={name} />
          </div>
        );
      })}
    </div>
  );
};

export default NameContainer;
