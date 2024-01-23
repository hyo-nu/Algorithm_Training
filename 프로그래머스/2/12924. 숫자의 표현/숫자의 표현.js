function solution(n) {
    let answer = 1
    for (let i = 1; i <= Math.floor(n/2); i++){
        let sum = i
        let num = i
        while (sum < n){
            num++
            sum += num
        }
        if (sum === n) answer++
    }
    return answer;
}