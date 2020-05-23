import React, { useState } from "react";
import "./App.css";
import List from "./List";
import Arjun from "./assets/Me.jpg"
import Dad from "./assets/Dad.png"
import Mom from "./assets/Mom.png"
import Ishan from "./assets/Ishan.png"
import Member from "./Member";


// This is the app:

const App = () => {


  const names = ["Arjun", "Dad", "Mom", "Ishan"];
  const description = ["Arjun likes to play basketball, football and tennis. He thinks school is BORING like most other kids.", "Dad runs Zebpay. He likes cryptocurrency.", "Mom is a doctor. She does the heart.", "Ishan likes math. He also likes science, TED and reading. He's basically a nerd."];
  const images = [Arjun, Dad, Mom, Ishan]
  // myobj is a list
  const myobj = [{name:names[0], description:description[0], image:images[0]}, {name:names[1], description:description[1], image:images[1]}, {name:names[2], description:description[2], image:images[2]}, {name:names[3], description:description[3], image:images[3]}]
  // for index, elem in enumerate(myobj): 
  //  print(elem) apples, bananas
  //  print(index) 0, 1,  

  return(<div>{myobj.map((obj)=> {
    return (
      <Member name={obj.name} description={obj.description} image={obj.image}></Member>
    )
  })}
  </div>)
};

export default App;
