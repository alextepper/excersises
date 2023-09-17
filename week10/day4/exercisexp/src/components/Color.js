import React from "react";

class Child extends React.Component {
  componentWillUnmount() {
    alert("Child component is being unmounted!");
  }

  render() {
    return <h1>Hello World!</h1>;
  }
}

class Color extends React.Component {
  constructor(props) {
    super(props);
    this.state = { favoriteColor: "red", show: true };
    this.changeColor = this.changeColor.bind(this);
    this.deleteChild = this.deleteChild.bind(this);
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({ favoriteColor: "yellow" });
    }, 1000);
  }

  componentDidUpdate() {
    console.log("after update");
  }

  changeColor() {
    this.setState({ favoriteColor: "blue" });
  }

  deleteChild() {
    this.setState({ show: false });
  }

  render() {
    return (
      <div>
        <h1>My Favorite color is {this.state.favoriteColor}</h1>
        <button onClick={this.changeColor}>Change Color</button>
        <div>
          {this.state.show && <Child />}

          <button onClick={this.deleteChild}>Delete</button>
        </div>
      </div>
    );
  }
}

export default Color;
