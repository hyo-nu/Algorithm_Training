function solution(s) {
    let cycle = 0, zeroCount = 0
    
    while (s !== "1"){
        let zeroDel = s.replaceAll("0","")
        let lenZeroDel = zeroDel.length
        zeroCount += (s.length - lenZeroDel)
        s = lenZeroDel.toString(2)
        cycle += 1
    }
    return [cycle,zeroCount];
}