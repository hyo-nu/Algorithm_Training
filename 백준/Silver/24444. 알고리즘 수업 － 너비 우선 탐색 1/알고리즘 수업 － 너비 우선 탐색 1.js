const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const fs = require("fs")
let input = fs.readFileSync(filePath).toString().trim().split("\n")

const [n, m, r] = input[0].split(" ").map(Number)
const G = Array.from({length: n + 1}, () => [])

for (let i = 1; i <= m; i++){
  const [sp,ep] = input[i].split(" ").map(Number)
  G[sp].push(ep)
  G[ep].push(sp)
}

G.forEach((line) => line.sort((a,b) => a - b))
const vi = new Array(n + 1).fill(0)

let Q = [r]
vi[r] = 1

let order = 1
while(Q.length) {
  const sp = Q.shift()
  for (const np of G[sp]){
    if(!vi[np]) {
      Q.push(np)
      vi[np] = ++order
    }
  }
}

console.log(vi.slice(1).join("\n"))