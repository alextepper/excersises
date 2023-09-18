import React, { Component } from "react";

export default class OutputInfo extends Component {
  render() {
    const {
      firstName,
      lastName,
      age,
      gender,
      destination,
      nutsFree,
      lactoseFree,
      isVegan,
    } = this.props.data;

    return (
      <div className="entered-info">
        <h2>Entered information:</h2>
        <p>
          Your name: {firstName} {lastName}
        </p>
        <p>Your age: {age}</p>
        <p>Your gender: {gender}</p>
        <p>Your destination: {destination}</p>
        <p>Your dietary restrictions:</p>
        <div className="restrictions">
          <span>**Nuts free : {nutsFree ? "Yes" : "No"}</span>
          <br />
          <span>**Lactose free : {lactoseFree ? "Yes" : "No"}</span>
          <br />
          <span>**Vegan meal : {isVegan ? "Yes" : "No"}</span>
        </div>
      </div>
    );
  }
}
