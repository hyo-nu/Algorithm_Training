function solution(brown, yellow) {
    const cnt = brown + yellow
    let height = 3, length = 0
    
    while(true) {
        if (cnt % height === 0) {
            length = cnt / height
            if ( (height-2) * (length-2) === yellow){
                break
            }
        }
        height++
    }
    
    return [length, height];
}