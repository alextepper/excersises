const chalk = require('chalk'); // chalk 4.1.2 otherwise it 

function displayColorfulMessage() {
  console.log(chalk.blue('This is a colorful message!'));
}

module.exports = displayColorfulMessage;
