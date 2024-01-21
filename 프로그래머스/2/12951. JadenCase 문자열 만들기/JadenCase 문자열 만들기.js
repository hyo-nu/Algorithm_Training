function solution(s) {
    var answer = '';
    
    const JadenCase = s.split(" ").map((str,idx) => {
        const tmp = str.split("").map((s,i) => {
            return i !== 0 ? s.toLowerCase() : !Number(s) ? s.toUpperCase() : s })
        return tmp.join("")
    })
    
    return JadenCase.join(" ");
}