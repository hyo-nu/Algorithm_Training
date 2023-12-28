function solution(s) {
    const nums =  ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    let number = "", alpha = ""
    s.split("").forEach((val) => {
        isNaN(Number(val)) ? alpha += val : number += val
        idx = nums.indexOf(alpha)
        idx !== -1 ? (number += String(idx),alpha = "") : ("")
    })
    return Number(number)
}

// function solution(s) {
//     const num = {
//         "zero" : "0",
//         "one" : "1",
//         "two" : "2",
//         "three" : "3",
//         "four" :"4",
//         "five" : "5",
//         "six" : "6",
//         "seven" : "7",
//         "eight" : "8",
//         "nine" : "9"
//     }
    
//     let result = ""
//     for(let i = 0; i < s.length; i++){
//         if(isNaN(s[i] * 10) === false) {
//             result += s[i]
//         }
//         else{
//             str = ""
//             while(isNaN(s[i] * 10)){
//                 str += s[i];
//                 if (num[str] !== undefined){
//                     result += num[str]
//                     break
//                 }
//                 i++;    
//             }
//         }
//     }
//     return parseInt(result);
// }