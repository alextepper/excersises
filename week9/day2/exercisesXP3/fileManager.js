const fs = require('fs');

function readFile(filePath, callback) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) throw err;
    callback(data);
  });
}

function writeFile(filePath, content, callback) {
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) throw err;
    callback();
  });
}

module.exports = {
  readFile,
  writeFile
};
