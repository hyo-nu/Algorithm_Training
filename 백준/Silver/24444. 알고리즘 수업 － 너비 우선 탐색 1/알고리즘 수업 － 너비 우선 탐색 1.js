const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const fs = require("fs")
let input = fs.readFileSync(filePath).toString().trim().split("\n")

class Queue{
  head = 0
  tail = 0
  list = []
  constructor(){}

  append(value){
    this.list[this.tail++] = value
  }
  popleft(){
    if(this.isEmpty()){
      return false
    }
    return this.list[this.head++]
  }
  isEmpty(){
    return this.head === this.tail ? true : false
  }
}

const [n, m, r] = input[0].split(" ").map((e) => Number(e))
const G = Array.from({length: n + 1}, () => [])
const vi = new Array(n + 1).fill(0)
let order = 1

for (let i = 1; i <= m; i++){
  const [sp,ep] = input[i].split(" ").map(Number)
  G[sp].push(ep)
  G[ep].push(sp)
}

G.forEach((line) => line.sort((a,b) => a - b))

let Q = new Queue()
Q.append(r)
vi[r] = 1

while(!Q.isEmpty()) {
  const sp = Q.popleft()
  for (const np of G[sp]){
    if(!vi[np]) {
      Q.append(np)
      vi[np] = ++order
    }
  }
}

console.log(vi.slice(1).join("\n"))