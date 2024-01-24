function solution(n) {
    const oneCnt = n.toString(2).replaceAll("0","")
    while (true){
        n++
        const nextOneCnt = n.toString(2).replaceAll("0","")
        if( oneCnt === nextOneCnt) {break}
    }
    return n;
}