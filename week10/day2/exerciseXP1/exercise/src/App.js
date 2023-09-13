import React from "react";
import UserFavoriteAnimals from "./UserFavoriteAnimals";
import Exercise from "./exercise3";

const user = {
  firstName: "Bob",
  lastName: "Dylan",
  favAnimals: ["Horse", "Turtle", "Elephant", "Monkey"],
};

function App() {
  return (
    <div className="App">
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <UserFavoriteAnimals animals={user.favAnimals} />
      <Exercise />
    </div>
  );
}

export default App;
