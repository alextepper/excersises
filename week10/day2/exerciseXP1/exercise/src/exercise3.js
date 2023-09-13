import React, { Component } from "react";
import "./exercise.css";

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial",
};

class Exercise extends Component {
  render() {
    return (
      <div>
        <h1 style={style_header}>This is a Header</h1>
        <p className="para">This is a Paragraph</p>
        <a href="#">This is a link</a>
        <form>
          <h2>This is a form</h2>
          <label>Enter your name:</label>
          <input type="text" placeholder="Sample input" />
          <button type="submit">Submit</button>
        </form>
        <h3>Here is an Image</h3>
        <img src="logo512.png" alt="Sample" />
        <h4>This is a list</h4>
        <ul>
          <li>Coffee</li>
          <li>Tea</li>
          <li>Milk</li>
        </ul>
      </div>
    );
  }
}

export default Exercise;
