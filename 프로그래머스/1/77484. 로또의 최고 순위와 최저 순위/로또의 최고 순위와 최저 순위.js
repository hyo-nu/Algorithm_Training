function solution(lottos, win_nums) {
    const rank = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    let correct = 0, zero = 0
    
    lottos.forEach((val) => {
        if(val === 0) { zero += 1}
        else if (win_nums.includes(val)) { correct += 1 }
    })
    
    return [rank[correct + zero],rank[correct]];
}