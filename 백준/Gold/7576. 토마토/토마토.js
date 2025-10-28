const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const [M, N] = inputs[0].split(' ').map(Number);
const graph = inputs.slice(1).map(input => input.split(' ').map(Number));

const queue = [];
for (let n = 0; n < N; n++) {
  for (let m = 0; m < M; m++) {
    if (graph[n][m] === 1) {
      queue.push([n, m]);
    }
  }
}

let head = 0;
const dr = [0, 0, -1, 1];
const dc = [1, -1, 0, 0];

while (head < queue.length) {
  const [r, c] = queue[head++];

  for (let d = 0; d < 4; d++) {
    const nr = r + dr[d];
    const nc = c + dc[d];

    if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
    if (graph[nr][nc] === 0) {
      graph[nr][nc] = graph[r][c] + 1;
      queue.push([nr, nc]);
    }
  }
}

let day = 0;
for (let n = 0; n < N; n++) {
  for (let m = 0; m < M; m++) {
    if (graph[n][m] === 0) {
      console.log(-1);
      return;
    }
    day = Math.max(day, graph[n][m]);
  }
}

console.log(day - 1);
