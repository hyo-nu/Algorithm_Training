const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const [N, M, R] = inputs[0].split(' ').map(Number);
const G = Array.from({ length: N + 1 }, () => []);

for (const edge of inputs.slice(1)) {
  const [u, v] = edge.split(' ').map(Number);
  G[u].push(v);
  G[v].push(u);
}

G.forEach(g => g.sort((a, b) => b - a));

const vi = Array(N + 1).fill(0);
let order = 1;

const s = [R];

while (s.length) {
  const v = s.pop();

  if (!vi[v]) {
    vi[v] = order++;

    for (let i = G[v].length - 1; i >= 0; i--) {
      const next = G[v][i];
      if (!vi[next]) {
        s.push(next);
      }
    }
  }
}

console.log(vi.slice(1).join('\n'));