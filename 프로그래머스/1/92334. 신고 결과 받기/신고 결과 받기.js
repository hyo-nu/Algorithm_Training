function solution(id_list, report, k) {
    let N = id_list.length
    const id_dict = {}
    id_list.forEach((value,idx) => id_dict[value] = idx )
    G = Array.from({length : N}, () => Array(N).fill(0))
    
    report.forEach((name,idx) => {
        const [report, receive] = name.split(" ")
        G[id_dict[report]][id_dict[receive]] = 1
    })
    
    const result = []
    for(let i = 0; i < N ; i ++ ){
        let people = 0
        for(let j = 0; j < N ; j ++ ){
            if (G[i][j] === 1) {
                let cnt = 0
                for (let l = 0; l < N; l++){
                    cnt += G[l][j]
                }
                if (cnt >= k) {people ++}
            }
        }
        result.push(people)
    }
    return result;
}