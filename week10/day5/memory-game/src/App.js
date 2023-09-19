import React, { Component } from "react";
import CharacterCard from "./components/CharacterCard";
import Wrapper from "./components/Wraper";
import Navbar from "./components/Navbar";
import Jumbotron from "./components/Jumbotron";
import charcterJson from "./superheroes.json";
import "./App.css";
const superheroes = charcterJson.superheroes;

class App extends Component {
  state = {
    superheroes,
    highScore: 0,
    currentScore: 0,
    Clicked: false,
  };

  handleClick = (id) => {
    this.shuffleArray();
    this.handleScore(id);
    console.log(this.state.timesClicked);
  };

  handleScore = (id) => {
    this.state.superheroes.forEach((element) => {
      if (id === element.id && element.clicked === false) {
        element.clicked = true;
        this.setState({ Clicked: false });
        this.handleIncrement();
      } else if (id === element.id && element.clicked === true) {
        if (this.state.currentScore > this.state.highScore) {
          this.setState({ highScore: this.state.currentScore });
        }
        this.setState({ currentScore: 0 });
        this.setState({ Clicked: true });
        this.state.superheroes.forEach((element) => (element.clicked = false));
        console.log(this.state.superheroes);
      }
    });
  };

  shuffleArray = () => {
    const shuffledArr = this.shuffle(this.state.superheroes);
    this.setState({ shuffledArr });
  };

  handleIncrement = () => {
    this.setState({ currentScore: this.state.currentScore + 1 });
  };

  shuffle = (array) => {
    var currentIndex = array.length,
      temporaryValue,
      randomIndex;

    while (0 !== currentIndex) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;

      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
    return array;
  };

  render() {
    console.log(typeof this.state.superheroes);
    return (
      <Wrapper>
        <Navbar
          currentScore={this.state.currentScore}
          highScore={this.state.highScore}
        />
        <Jumbotron />
        {this.state.superheroes.map((superhero) => (
          <CharacterCard
            Clicked={this.state.Clicked}
            handleClick={this.handleClick}
            id={superhero.id}
            key={superhero.id}
            name={superhero.name}
            image={superhero.image}
            occupation={superhero.occupation}
          />
        ))}
      </Wrapper>
    );
  }
}

export default App;
