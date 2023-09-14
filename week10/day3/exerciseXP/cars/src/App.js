import React from "react";
import Car from "./components/Car";
import Events from "./components/Events";
import Phone from "./components/Phone";
import Color from "./components/Color";

const carinfo = { name: "Ford", model: "Mustang" };

function App() {
  return (
    <div className="App">
      <Car car={carinfo} />
      <Events />
      <Phone />
      <Color />
    </div>
  );
}

export default App;
