function solution(answers) {
    const math1 = Array.from({ length: Math.ceil(answers.length / 5) * 5 }, (_, i) => [1,2,3,4,5][i % 5]);
    const math2 = Array.from({ length: Math.ceil(answers.length / 8) * 8 }, (_, i) => [2,1,2,3,2,4,2,5][i % 8]);
    const math3 = Array.from({ length: Math.ceil(answers.length / 10) * 10 }, (_, i) => [3,3,1,1,2,2,4,4,5,5][i % 10]);
    
    let scores = [0, 0, 0]
    answers.forEach((value, index) => {
        if (value === math1[index]) {scores[0] += 1}
        if (value === math2[index]) {scores[1] += 1}
        if (value === math3[index]) {scores[2] += 1}
    })
    
    let result = [] 
    scores.forEach((value,idx) => Math.max(...scores) === value ? result.push(idx+1) :"")
    
    return result;
}