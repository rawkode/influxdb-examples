import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  fetch("http://influxdb.com:9999/api/v2/query?org=rawkode", {
    headers: {
      "Content-Type": "application/vnd.flux",
      Origin: "http://myapp.com",
      Authorization:
        "Token WwCEGtBcz6NqwDbkLsIRE84xOXYg_F3Dkmu7USPniMn8JyEAMlob33Nq_3D0wg0d5HfyDvZWd3586HxK9HOS3Q=="
    }
  })
    .then(response => {
      return response.json();
    })
    .then(myJson => {
      console.log(myJson);
    });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
