import React, { useState } from "react";

const Events = () => {
  const [isToggleOn, setIsToggleOn] = useState(true);

  const clickMe = () => {
    alert("I was clicked");
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      alert(`You entered: ${event.target.value}`);
    }
  };

  const toggleButton = () => {
    setIsToggleOn(!isToggleOn);
  };

  return (
    <div>
      <div>
        <button onClick={clickMe}>Click me</button>
      </div>
      <div>
        <input
          type="text"
          onKeyDown={handleKeyDown}
          placeholder="Type something and press Enter"
        />
      </div>
      <div>
        <button onClick={toggleButton}>{isToggleOn ? "ON" : "OFF"}</button>
      </div>
    </div>
  );
};

export default Events;
