const fs = require('fs');

const inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const alphaSet = new Set(inputs.slice(1));

const alphaArray = [...alphaSet];

const G = Array.from({ length: 51 }, () => []);

for (const alpha of alphaArray) {
  G[alpha.length].push(alpha);
}

for (const alphas of G) {
  if (alphas.length > 0) {
    alphas.sort();
  }
}
let resultArray = [];
for (const alphas of G) {
  resultArray = resultArray.concat(alphas);
}

console.log(resultArray.join('\n'));