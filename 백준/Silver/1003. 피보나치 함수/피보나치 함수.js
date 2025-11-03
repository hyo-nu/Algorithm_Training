const fs = require('fs');

let inputs = fs.readFileSync(0).toString().trim().split('\n').map(Number);

for (const number of inputs.slice(1)) {
  const result = Array.from({ length: 41 }, () => [0, 0]);
  for (let n = 0; n <= number; n++) {
    if (n <= 1) {
      result[n][n]++;
    } else {
      result[n][0] = result[n - 2][0] + result[n - 1][0];
      result[n][1] = result[n - 2][1] + result[n - 1][1];
    }
  }
  console.log(result[number].join(' '));
}