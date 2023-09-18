import React, { Component } from "react";

export default class RestrictionInput extends Component {
  handleInputChange = (event) => {
    const target = event.target;
    const value = target.checked;
    const name = target.name;

    this.props.onInputChange(name, value);
  };

  render() {
    return (
      <div>
        <label className="restrictions-title">Dietary restrictions:</label>
        <br />
        <div className="restrictions">
          <input
            type="checkbox"
            name="nutsFree"
            checked={this.props.data.nutsFree}
            onChange={this.handleInputChange}
          />
          <span>Nuts free</span>
          <br />
          <input
            type="checkbox"
            name="lactoseFree"
            checked={this.props.data.lactoseFree}
            onChange={this.handleInputChange}
          />
          <span>Lactose free</span>
          <br />
          <input
            type="checkbox"
            name="isVegan"
            checked={this.props.data.isVegan}
            onChange={this.handleInputChange}
          />
          <span>Vegan</span>
        </div>
      </div>
    );
  }
}
