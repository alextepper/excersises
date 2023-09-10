const fs = require('fs');

function displayFileContent() {
  fs.readFile('./files/file-data.txt', 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading the file:', err);
      return;
    }
    console.log(data);
  });
}

module.exports = displayFileContent;
