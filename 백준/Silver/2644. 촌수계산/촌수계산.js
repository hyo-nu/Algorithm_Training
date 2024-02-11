const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const fs = require("fs")
let input = fs.readFileSync(filePath).toString().trim().split("\n")

const [N] = input[0].split(" ").map((e) => Number(e))
const [sp,ep] = input[1].split(" ").map((e) => Number(e))
const [M] = input[2].split(" ").map((e) => Number(e))
let G = Array.from({length : N + 1}, () => [])
let vi = Array(N+1).fill(0)

for(let i = 0; i < M; i++) {
  const [u, v] = input[i+3].split(" ").map((e) => Number(e))
  G[u].push(v)
  G[v].push(u)
}

let Q = [sp]
vi[sp] = 1

while(Q.length){
  const sp = Q.shift()
  for(const np of G[sp]){
    if(!vi[np]){
      Q.push(np)
      vi[np] = vi[sp] + 1
    }
  }
}
console.log(vi[ep]-1)