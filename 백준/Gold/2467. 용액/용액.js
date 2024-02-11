const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const fs = require("fs")
let input = fs.readFileSync(filePath).toString().trim().split("\n")

const [n] = input[0].split(" ").map((e) => Number(e))
const nums = input[1].split(" ").map((e) => Number(e))

let sp = 0, ep = n - 1
let zero = 2000000001
let result = []

while(sp < ep) {
  const value = nums[sp] + nums[ep]
  
  if (zero > Math.abs(value)){
    zero = Math.abs(value)
    result = [nums[sp] , nums[ep]]
  } 

  if (value <= 0){
    sp++
  }
  
  else if (value > 0){
    ep--
  }
}

console.log(...result)