import React, { Component } from "react";
import "./App.css";
import NameInput from "./Components/NameInput";
import GenderInput from "./Components/GenderInput";
import DestinantionInput from "./Components/DestinantionInput";
import RestrictionInput from "./Components/RestrictionInput";
import OutputInfo from "./Components/OutputInfo";

class App extends Component {
  constructor() {
    super();
    this.state = {
      data: {
        firstName: "",
        lastName: "",
        age: "",
        gender: "",
        destination: "",
        nutsFree: false,
        lactoseFree: false,
        isVegan: false,
      },
    };
  }

  handleInputChange = (field, value) => {
    this.setState((prevState) => ({
      data: {
        ...prevState.data,
        [field]: value,
      },
    }));
  };

  render() {
    return (
      <div className="App">
        <h1>Sample form</h1>
        <form className="inputForm">
          <NameInput
            data={this.state.data}
            onInputChange={this.handleInputChange}
          />
          <GenderInput
            data={this.state.data}
            onInputChange={this.handleInputChange}
          />
          <DestinantionInput
            data={this.state.data}
            onInputChange={this.handleInputChange}
          />
          <RestrictionInput
            data={this.state.data}
            onInputChange={this.handleInputChange}
          />
          <button className="submit">Submit</button>
        </form>
        <OutputInfo data={this.state.data} />
      </div>
    );
  }
}

export default App;
