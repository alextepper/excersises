const fs = require('fs');

// Read the list of files in the current directory
fs.readdir('.', (err, files) => {
  if (err) {
    console.error('Error reading the directory:', err);
    return;
  }

  // Display the file names
  console.log('Files in the directory:', files.join(', '));
});
