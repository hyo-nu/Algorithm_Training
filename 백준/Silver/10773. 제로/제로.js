const fs = require('fs');

const inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => parseInt(input.trim()));

const N = inputs[0];

const array = [];

for (const num of inputs.slice(1)) {
  if (num === 0) {
    array.pop();
  } else {
    array.push(num);
  }
}

const sum = array.reduce((acc, cur) => acc + cur, 0);
console.log(sum);