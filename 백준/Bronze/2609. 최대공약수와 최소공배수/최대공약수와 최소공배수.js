const fs = require('fs');
let [A, B] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

let num = 2;
let result = 1;

while (num <= A && num <= B) {
  if (A % num === 0 && B % num === 0) {
    A /= num;
    B /= num;
    result *= num;
  } else {
    num++;
  }
}

console.log(result);
console.log(result * A * B);