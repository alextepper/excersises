import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import Color from "./components/Color";

if (
  window.__REACT_DEVTOOLS_GLOBAL_HOOK__ &&
  typeof window.__REACT_DEVTOOLS_GLOBAL_HOOK__ === "object"
) {
  window.__REACT_DEVTOOLS_GLOBAL_HOOK__.inject = function () {};
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
    <Color />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
