function solution(s, skip, index) {
    result = ""
    Array.from(s).forEach((alpha) => {
        let chage = 1, pass = 0
        while (chage <= index){
            if (Array.from(skip).includes(String.fromCharCode((alpha.charCodeAt()+chage+pass-97) % 26 + 97))){
                pass++
            }
            else {
                chage ++
            }
        }
        result += String.fromCharCode(((alpha.charCodeAt() + chage + pass - 98) % 26) + 97)
    })    
    return result;
}  