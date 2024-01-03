function solution(N, stages) {
    let arrives = new Array(N + 2).fill(0)
    stages.forEach((stage) => arrives[stage] += 1)
    
    let result = [], remain = stages.length
    for(let i = 1; i <= N ; i++){
        console.log(arrives[i], remain)
        result.push([i, arrives[i] / remain])
        remain -= arrives[i]
    }
    result.sort((a,b) => b[1] - a[1])
    
    return result.map(([stage,percent]) => stage);
}