const fs = require('fs');

const number = parseInt(fs.readFileSync(0).toString());

for (let i = 1; i <= number; i++) {
  console.log(i);
}