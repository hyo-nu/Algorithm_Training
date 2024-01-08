function solution(keymap, targets) {
    
    
    const answer = targets.map((alpha,a_idx) => {
        let click = 0
        for(let i = 0; i < alpha.length; i++){
            const press = keymap.map((key,k_idx) => {
                for(let j=0; j < key.length; j++){
                    if(key[j] === alpha[i]){return (j+1)}
                }
                return 101
            })
            let Min = Math.min(...press)
            if(Min !== 101){click += Min}
            else {
                click = -1
                break
            }
        }
        return click
    })
    return answer;
}