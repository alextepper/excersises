import React, { Component } from "react";

export default class DestinationInput extends Component {
  handleDestinationChange = (event) => {
    this.props.onInputChange("destination", event.target.value);
  };

  render() {
    return (
      <div>
        <label className="destination-header">Select your destination</label>
        <br />
        <select
          className="destination-input"
          name="destination"
          value={this.props.data.destination}
          onChange={this.handleDestinationChange}
        >
          <option value="">-- Please Choose a destination --</option>
          <option value="Thailand">Thailand</option>
          <option value="Japan">Japan</option>
          <option value="Brazil">Brazil</option>
        </select>
      </div>
    );
  }
}
