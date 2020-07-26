import React, { useState, useEffect } from "react";
import "./App.css";
import Arjun from "./assets/Me.jpg";
import Dad from "./assets/Dad.png";
import Mom from "./assets/Mom.png";
import Ishan from "./assets/Ishan.png";
import Member from "./components/Member";
import { makeStyles } from "@material-ui/core/styles";
import GridList from "@material-ui/core/GridList";
import { weatherAPIKey, locationAPIKey } from "./password";
import NavBar from "./components/NavBar/NavBar";
import { Switch, Route } from "react-router-dom";
import SideDrawer from "./components/SideDrawer/SideDrawer";
import Backdrop from "./components/Backdrop/Backdrop";

// This is the app:

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "center",
    overflow: "hidden",
    backgroundColor: theme.palette.background.paper,
  },
  gridList: { width: "100vw", height: "100vh" },
}));

const App = () => {
  // const state = {
  //   sideDrawerOpen: false,
  // };

  const [sideDrawerOpen, setSideDrawerOpen] = useState(false);
  const drawerToggleClickHandler = () => {
    setSideDrawerOpen(!sideDrawerOpen);
  };

  const closeSideDrawer = () => {
    setSideDrawerOpen(false);
  };

  const [temp, setTemp] = useState("");
  const [tempMax, setTempMax] = useState("");
  const [tempMin, setTempMin] = useState("");
  const [clouds, setClouds] = useState("");
  const [coords, setCoords] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [country, setCountry] = useState("");
  const [ip, setIp] = useState("");
  const [zipCode, setZipCode] = useState("");

  const convertTemp = (cels) => {
    return (cels * 9) / 5 + 32;
  };
  const getCoords = async () => {
    var url = "https://ipinfo.io?token=" + locationAPIKey;
    const api_call = await fetch(url);
    const data = await api_call.json();
    const location = data["loc"];
    const [lat, lng] = location.split(",");
    // console.log(lat, lng);
    // console.log(data);
    const { city, country, ip, postal, region, timezone } = data;
    // console.log(city, country);
    return {
      city: city,
      country: country,
      lat: lat,
      lng: lng,
      ip: ip,
      postal: postal,
      region: region,
      timezone: timezone,
    };
  };

  const getWeather = async () => {
    const location = await getCoords();
    const { city, country, lat, lng, ip, postal, region, timezone } = location;
    fetch(
      `http://api.openweathermap.org/data/2.5/weather?q=${city},${country}&appid=${weatherAPIKey}&units=metric`
    )
      .then((weather) => {
        return weather.json();
      })
      .then((weather) => {
        // console.log(weather);
        // call useState method here, and data automatically shows on website
        setTemp(convertTemp(weather.main.temp));
        setTempMax(convertTemp(weather.main.temp_max));
        setTempMin(convertTemp(weather.main.temp_min));
        setClouds(weather.clouds.all);
        setCoords(lat + ", " + lng);
        setCity(city);
        setCountry(country);
        setIp(ip);
        setZipCode(postal);
        setState(region);
      });
  };

  // creating a function that will ONLY be called when the website launches for the first time only
  useEffect(() => {
    getWeather();
    getCoords();
  }, []);

  const nornot = ["", "n", "n", "n"];
  const classes = useStyles();
  const names = ["Arjun", "Dad", "Mom", "Ishan"];
  const description = [
    "Arjun likes to play basketball, football and tennis.",
    "Dad runs Zebpay. He likes cryptocurrency.",
    "Mom is a doctor. She does the heart.",
    "Ishan likes math. He also likes science, TED and reading. He's smart.",
  ];
  const images = [Arjun, Dad, Mom, Ishan];

  const embarrassingorfun = ["Fun", "Fun", "Fun", "Fun"];

  const secrets = [
    "Arjun beat a 7th grader at basketball",
    "Dad runs Zebpay",
    "Mom lived in India for a year after college",
    "Ishan can edit a video",
  ];
  // myobj is a list
  const myobj = [
    {
      name: names[0],
      description: description[0],
      image: images[0],
      secret: secrets[0],
      embarrassingorfun: embarrassingorfun[0],
      nornot: nornot[0],
    },
    {
      name: names[1],
      description: description[1],
      image: images[1],
      secret: secrets[1],
      embarrassingorfun: embarrassingorfun[1],
      nornot: nornot[1],
    },
    {
      name: names[2],
      description: description[2],
      image: images[2],
      secret: secrets[2],
      embarrassingorfun: embarrassingorfun[2],
      nornot: nornot[2],
    },
    {
      name: names[3],
      description: description[3],
      image: images[3],
      secret: secrets[3],
      embarrassingorfun: embarrassingorfun[3],
      nornot: nornot[3],
    },
  ];
  // for index, elem in enumerate(myobj):
  //  print(elem) apples, bananas
  //  print(index) 0, 1,

  //   <div className={classes.root}>
  //   <GridList className={classes.gridList} cols={2}>
  //     {mylist.map((value) => {
  //       return <div style={{ height: "50vh", width: "49.5vw" }}>{value}</div>;
  //     })}
  //   </GridList>
  // </div>

  let backdrop;

  if (sideDrawerOpen) {
    backdrop = <Backdrop toggle={closeSideDrawer} />;
  }

  return (
    <div className="App" style={{ height: "100%" }}>
      <NavBar toggle={drawerToggleClickHandler} object={myobj} />
      <SideDrawer show={sideDrawerOpen} toggle={closeSideDrawer} />
      {backdrop}
      <Switch>
        <Route
          exact
          path="/"
          render={() => (
            <div className={classes.root}>
              <GridList className={classes.gridList} cols={2}>
                {myobj.map((obj) => {
                  return (
                    <Member
                      name={obj.name}
                      description={obj.description}
                      image={obj.image}
                      secret={obj.secret}
                      embarrassingorfun={obj.embarrassingorfun}
                      nornot={obj.nornot}
                    ></Member>
                  );
                })}
              </GridList>
            </div>
          )}
        />
        <Route
          path="/weather"
          render={() => (
            <span style={{ textAlign: "center", marginTop: "2rem" }}>
              <h3>This is the temperature maximum: {tempMax}°</h3>
              <h3>This is the temperature: {temp}°</h3>
              <h3 style={{ marginBottom: "1rem" }}>
                This is the temperature minimum: {tempMin}°
              </h3>
              <h3>This is how many clouds are in your city: {clouds}</h3>
              <h3>These are your city's coordinates: {coords}</h3>
              <h3>This is your city: {city}</h3>
              <h3>This is your state: {state}</h3>
              <h3>This is your country: {country}</h3>
              <h3>
                This is your location: {city}, {state}, {country}
              </h3>
              <h3>This is your ip: {ip}</h3>
              <h3>This is your zip code: {zipCode}</h3>
              <p>*We are not always exactly accurate</p>
            </span>
          )}
        />
      </Switch>
    </div>
  );
};

export default App;
