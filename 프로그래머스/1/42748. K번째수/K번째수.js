function solution(array, commands) {
    return commands.map(([i, j, k]) => array.slice(i-1, j).sort((a,b) => a-b)[k-1])    
}

// function solution(array, commands) {
//     answer = []
//     for (let i = 0; i < commands.length; i++){
//         let a = commands[i][0], b = commands[i][1], k = commands[i][2]
//         let arr = array.slice(a-1,b)
//         arr.sort((a,b) => a-b)
//         answer.push(arr[k-1])
//     }
//     return answer
// }