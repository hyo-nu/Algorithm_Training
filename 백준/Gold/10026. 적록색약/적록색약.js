const fs = require('fs');

let inputs = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map(input => input.trim());

const BFS = (r, c, vi, color, RGB) => {
  const dr = [0, 0, 1, -1];
  const dc = [1, -1, 0, 0];
  const queue = [];
  let head = 0;

  vi[r][c] = 1;
  queue.push([r, c]);

  while (head < queue.length) {
    const [rr, cc] = queue[head++];

    for (let d = 0; d < 4; d++) {
      const nr = rr + dr[d];
      const nc = cc + dc[d];

      if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
      if (!vi[nr][nc]) {
        if (G[nr][nc] === color) {
          vi[nr][nc] = 1;
          queue.push([nr, nc]);
        } else if (RGB && (color === 'R' || color === 'G') && G[nr][nc] !== 'B') {
          vi[nr][nc] = 1;
          queue.push([nr, nc]);
        }
      }
    }
  }
};

const N = parseInt(inputs[0]);
const G = inputs.slice(1).map(input => input.split(''));

const RGB = Array.from({ length: N }, () => Array(N).fill(0));
const RRB = Array.from({ length: N }, () => Array(N).fill(0));

let rgbCount = 0;
let rrbCount = 0;

for (let r = 0; r < N; r++) {
  for (let c = 0; c < N; c++) {
    if (!RGB[r][c]) {
      rgbCount++;
      BFS(r, c, RGB, G[r][c], false);
    }

    if (!RRB[r][c]) {
      rrbCount++;
      BFS(r, c, RRB, G[r][c], true);
    }
  }
}

console.log(rgbCount, rrbCount);