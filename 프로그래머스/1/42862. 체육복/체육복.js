function solution(n, lost, reserve) {
    let cl = Array.from({length : n+2}, (val,idx) => idx === 0 || idx === n+1 ? 0 : 1)
    lost.forEach((val) => cl[val] = 0)
    reserve.forEach((val) => cl[val] += 1)
    
    let cnt = 0
    for (let i = 1; i <= n ; i++) {
        if (cl[i] === 0){
            if(cl[i-1] === 2){
                cl[i-1] -= 1
                cl[i] += 1
            }
            else if(cl[i+1] === 2){
                cl[i+1] -= 1
                cl[i] += 1
            }
        }
        if (cl[i] >= 1) {
            cnt += 1
        }
    }
    return cnt;
}