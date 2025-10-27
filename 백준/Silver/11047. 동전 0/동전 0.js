const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const [N, K] = inputs[0].split(' ').map(Number);
const coins = inputs.slice(1).map(Number);

let count = 0;
let money = 0;

for (let i = N - 1; i >= 0; i--) {
  while (money + coins[i] <= K) {
    money += coins[i];
    count++;
  }
}

console.log(count);