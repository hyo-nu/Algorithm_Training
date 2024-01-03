function solution(n, m, section) {
    
    let sp = 0, pos = 0, paint = 0
    
    while (sp <= section.length - 1){
        if (pos <= section[sp]){
            paint += 1
            pos = section[sp] + m
        }
        sp += 1
    }
    return paint;
}