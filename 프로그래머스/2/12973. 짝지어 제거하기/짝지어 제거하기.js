function solution(s)
{
    let str = []
    
    s.split("").forEach((val,idx) => {
        if (str.length > 0){
            if (str[str.length-1] === val) {
                str.pop()
            }
            else {str.push(val)}
        }
        else {str.push(val)}
    })
    return str.length <= 0 ? 1 : 0;
}