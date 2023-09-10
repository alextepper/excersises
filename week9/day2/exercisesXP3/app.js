const { readFile, writeFile } = require('./fileManager.js');

// Read from 'Hello World.txt'
readFile('Hello World.txt', (content) => {
  console.log('Content of "Hello World.txt":', content);

  // Write to 'Bye World.txt'
  writeFile('Bye World.txt', 'Writing to the file', () => {
    console.log('Written to "Bye World.txt" successfully.');
  });
});
