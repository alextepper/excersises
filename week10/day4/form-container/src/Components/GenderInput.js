import React, { Component } from "react";

export default class GenderInput extends Component {
  handleGenderChange = (event) => {
    this.props.onInputChange("gender", event.target.value);
  };

  render() {
    return (
      <div>
        <label>
          <input
            className="radiobutton"
            type="radio"
            name="gender"
            value="male"
            checked={this.props.data.gender === "male"}
            onChange={this.handleGenderChange}
          />
          Male
        </label>
        <br />
        <label>
          <input
            className="radiobutton"
            type="radio"
            name="gender"
            value="female"
            checked={this.props.data.gender === "female"}
            onChange={this.handleGenderChange}
          />
          Female
        </label>
      </div>
    );
  }
}
