function solution(arr){
    return arr.filter((val,index) => val != arr[index + 1])
}

// function solution(arr){
//     arr2 = []
    
//     let same = -1
//     for (let i = 0; i < arr.length; i++){
//         if (same !== arr[i]){
//             arr2.push(arr[i])
//             same = arr[i]
//         }
//     }
//     return arr2
// }

// function solution(arr)
// {
//     let ans = []
    
//     for (let i = 0; i < arr.length; i++ ){
//         if (arr[i] !== ans[ans.length-1] ) {
//             ans.push(arr[i])
//         }
//     }
//     return ans;
// }