const fs = require('fs');

const [a, b] = fs.readFileSync(0).toString().trim().split(' ');

console.log(parseInt(a) + parseInt(b));
