function solution(s) {
    const numbers = s.split(" ").sort((a,b) => a-b)
    const result = [numbers[0],numbers[numbers.length-1]].join(" ")
    
    return result;
}