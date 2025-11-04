const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const [N, M, V] = inputs[0].split(' ').map(Number);
const edges = Array.from({ length: N + 1 }, () => []);

for (const input of inputs.slice(1)) {
  const [a, b] = input.split(' ').map(Number);
  edges[a].push(parseInt(b));
  edges[b].push(parseInt(a));
}

edges.map(edge => edge.sort((a, b) => a - b));

const vi = Array(N + 1).fill(0);

vi[V] = 1;
let head = 0;
const queue = [V];

while (head < queue.length) {
  const v = queue[head++];

  for (const edge of edges[v]) {
    if (!vi[edge]) {
      queue.push(edge);
      vi[edge] = 1;
    }
  }
}

const vi2 = Array(N + 1).fill(0);

const stack = [V];
const result = [];
while (stack.length) {
  const v = stack.pop();

  if (vi2[v]) continue; // ✅ 이미 방문했으면 스킵
  vi2[v] = 1; // ✅ pop 시점에 방문 처리
  result.push(v);

  // ✅ 오름차순 방문을 위해 역순으로 push
  for (let i = edges[v].length - 1; i >= 0; i--) {
    const next = edges[v][i];
    if (!vi2[next]) stack.push(next); // ❗ push할 때는 방문 처리하지 않음
  }
}

console.log(result.join(' '));
console.log(queue.join(' '));
