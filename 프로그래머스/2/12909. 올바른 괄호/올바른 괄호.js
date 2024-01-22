function solution(s){
    let stack  = []
    
    s.split("").forEach((bracket,idx) => {
        if(bracket === "(") stack.push(bracket)
        else{
            if (stack.length >= 1) {
                stack.pop()
            }
            else {
                stack.push(")")
                return false
            }
        }
    })
    return stack.length === 0 ? true : false;
}