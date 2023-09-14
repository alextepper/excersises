import React, { useState } from "react";

const App = () => {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaScript", votes: 0 },
    { name: "Java", votes: 0 },
  ]);

  const voteForLanguage = (languageName) => {
    setLanguages(
      languages.map((language) => {
        if (language.name === languageName) {
          return { ...language, votes: language.votes + 1 };
        } else {
          return language;
        }
      })
    );
  };

  return (
    <div id="root">
      <h1>Vote Your Language!</h1>
      <div className="languages">
        {languages.map((language) => (
          <div key={language.name} className="language">
            <div className="voteCount">{language.votes}</div>
            <div className="languageName">{language.name}</div>
            <button onClick={() => voteForLanguage(language.name)}>
              Click Here
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
