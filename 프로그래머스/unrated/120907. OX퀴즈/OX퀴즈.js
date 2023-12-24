function solution(quiz) {
    let result = []
    
    for (let i = 0; i < quiz.length; i++){
        quiz[i] = quiz[i].split(" ")
        let X = Number(quiz[i][0]), Y = Number(quiz[i][2]), Z = Number(quiz[i][4])
        
        if (quiz[i][1] === "-"){
            if (X - Y === Z) { result.push("O")}
            else if (X - Y !== Z) { result.push("X")}
        }
        else if (quiz[i][1] === "+"){
            if (X + Y === Z) { result.push("O")}
            else if (X + Y !== Z) { result.push("X")}
        }
    }
    return result;
}