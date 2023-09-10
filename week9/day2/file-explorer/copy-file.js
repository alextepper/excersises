const fs = require('fs');

// Read the content from source.txt
fs.readFile('source.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

  // Write the same content to destination.txt
  fs.writeFile('destination.txt', data, (err) => {
    if (err) {
      console.error('Error writing to destination.txt:', err);
      return;
    }
    console.log('Content copied to destination.txt successfully!');
  });
});
