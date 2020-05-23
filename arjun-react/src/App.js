import React, { useState } from "react";
import "./App.css";
import List from "./List";

import basketball from "./basketballreact.png";
import baseball from "./baseball.png";

import Member from "./Member";




const App = () => {


  const names = ["Arjun", "Dad", "Mom", "Ishan"];
  const description = ["Arjun likes to play basketball, football and tennis. He thinks school is BORING like most other kids.", "Dad runs Zebpay. He likes cryptocurrency.", "Mom is a doctor. She does the heart.", "Ishan likes math. He also likes science, TED and reading. He's basically a nerd."];
  
  const myobj = [{name:"Arjun", description: "Arjun likes basketball"}, {name:"Dad", description:"Dad runs Zebpay"}]
  return(<div>{myobj.map( detailsobj=> {

    return(
    <Member name={detailsobj.name} description={detailsobj.description}></Member>
    )
    

  })}
  </div>)
};

export default App;
