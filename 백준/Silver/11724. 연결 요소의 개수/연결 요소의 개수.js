const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const [N, M] = inputs[0].split(' ').map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
const vi = Array(0).fill(0);

for (const input of inputs.slice(1)) {
  const [u, v] = input.split(' ');
  graph[u].push(parseInt(v));
  graph[v].push(parseInt(u));
}

const dfs = sp => {
  const stack = [sp];
  vi[sp] = 1;

  while (stack.length > 0) {
    const v = stack.pop();

    for (let i = graph[v].length - 1; i >= 0; i--) {
      const np = graph[v][i];
      if (!vi[np]) {
        stack.push(np);
        vi[np] = 1;
      }
    }
  }
};

let componetCnt = 0;
for (let i = 1; i <= N; i++) {
  if (!vi[i]) {
    componetCnt++;
    dfs(i);
  }
}

console.log(componetCnt);