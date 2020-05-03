import React, { useState } from "react";
import "./App.css";
import List from "./List";
import basketball from "./basketballreact.png";

const App = () => {
  const [toggle, setToggle] = useState(true);

  const printStatement = () => {
    setToggle("Arjun!");
    console.log(toggle);
  };

  return (
    <div>
      <div>
        <h1 style={{ textAlign: "center" }}>Arjun</h1>
      </div>
      <List basketball="basketball" football="football" guitar="guitar"></List>
      <button onClick={() => setToggle(!toggle)}>Toggle</button>
      {toggle ? <h1>toggle is true</h1> : <h1>toggle is false</h1>}
      <img src={basketball} width={100} height={100}></img>
    </div>
  );
};

export default App;
