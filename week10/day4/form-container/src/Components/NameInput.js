import React, { Component } from "react";

export default class NameInput extends Component {
  render() {
    return (
      <div>
        <input
          className="text"
          name="firstName"
          placeholder="First Name"
          value={this.props.data.firstName}
          onChange={(e) =>
            this.props.onInputChange("firstName", e.target.value)
          }
        />
        <br />
        <input
          className="text"
          name="lastName"
          placeholder="Last Name"
          value={this.props.data.lastName}
          onChange={(e) => this.props.onInputChange("lastName", e.target.value)}
        />
        <br />
        <input
          className="text"
          name="age"
          placeholder="Age"
          value={this.props.data.age}
          onChange={(e) => this.props.onInputChange("age", e.target.value)}
        />
      </div>
    );
  }
}
