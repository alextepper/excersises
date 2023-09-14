import React, { useState, useEffect } from "react";

const Color = () => {
  const [favoriteColor, setFavoriteColor] = useState("red");

  useEffect(() => {
    alert("useEffect reached");
  }, []); // The empty array ensures that useEffect is only called on the initial render

  const changeColor = () => {
    setFavoriteColor("blue");
  };

  return (
    <div>
      <h1>My Favorite color is {favoriteColor}</h1>
      <button onClick={changeColor}>Change Color</button>
    </div>
  );
};

export default Color;
