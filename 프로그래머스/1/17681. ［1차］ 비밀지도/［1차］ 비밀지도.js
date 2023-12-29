function solution(n, arr1, arr2) {
    const Map = arr1.map((num1,idx) => {
        bin1 = num1.toString(2).padStart(n, "0").split("")
        bin2 = arr2[idx].toString(2).padStart(n, "0").split("")
        
        password = ""
        for (let i = 0; i < n; i++){
            if(bin1[i] === '0' && bin2[i] === '0'){password += " "}
            else {password += "#"}
        }
        return password
    })
    return Map
}

// function solution(n, arr1, arr2) {
//     let G = Array.from(Array(n), () => Array())
    
//     for(let i = 0; i < n; i++){
//         bin1 = arr1[i].toString(2)
//         bin2 = arr2[i].toString(2)
//         if(bin1.length < n) {bin1 = ("0".repeat(n - (bin1.length))) + bin1}
//         if(bin2.length < n) {bin2 = ("0".repeat(n - (bin2.length))) + bin2}
        
//         for(let j = 0; j < n; j++){
//             if(bin1[j] === "0" && bin2[j] === "0") {
//                 G[i] += " "
//             }
//             else {
//                 G[i] += "#" 
//             }
//         }
//     }
//     console.log(G)
//     return G;
// }