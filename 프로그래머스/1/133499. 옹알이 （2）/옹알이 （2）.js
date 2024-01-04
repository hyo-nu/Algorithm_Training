function solution(babbling) {
    const accents = ["aya", "ye", "woo", "ma" ]
    const checks = babbling.map((str,s_idx) => {
        return accents.reduce((newAccent,curAccent,a_idx) => {
            return newAccent.replaceAll(curAccent,String(a_idx + 1))},str)})
    
    console.log(checks)
    let cnt = 0 
    checks.forEach((val) => {
        if(!!Number(val)){
            let stop = 0
            for(let i = 0; i <= String(val).length - 1 ; i ++){
                if (String(val)[i] === String(val)[i+1]){
                    stop = 1
                    break
                }
            }
            if(stop === 0) { cnt += 1}
        }
    })
    
    return cnt;
}