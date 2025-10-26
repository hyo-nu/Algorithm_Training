const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const BFS = (r, c, height, visited) => {
  const dr = [-1, 1, 0, 0];
  const dc = [0, 0, -1, 1];

  const queue = [[r, c]];
  visited[r][c] = 1;

  while (queue.length) {
    const [rr, cc] = queue.shift();
    for (let d = 0; d < 4; d++) {
      const nr = rr + dr[d];
      const nc = cc + dc[d];

      if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
      if (region[nr][nc] > height && !visited[nr][nc]) {
        visited[nr][nc] = 1;
        queue.push([nr, nc]);
      }
    }
  }
};

const N = parseInt(inputs[0]);
const region = inputs.slice(1).map(input => input.split(' ').map(Number));

let maxRegionCount = 0;
for (let height = 0; height <= 100; height++) {
  const visited = Array.from({ length: N }, () => Array(N).fill(0));
  let regionCount = 0;

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (region[r][c] > height && !visited[r][c]) {
        BFS(r, c, height, visited);
        regionCount++;
      }
    }
  }
  maxRegionCount = Math.max(maxRegionCount, regionCount);
}

console.log(maxRegionCount);