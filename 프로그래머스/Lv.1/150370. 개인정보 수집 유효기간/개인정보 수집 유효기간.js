function solution(today, terms, privacies) {
    const [ny, nm, nd] = today.split(".").map(Number)
    const Type = {}
    let result = []
    
    terms.forEach((info,idx) => {
        const [alpha, month] = info.split(" ")
        Type[alpha] = Number(month)
    })
    
    const totalDate = nd + (nm * 28) + (ny * 12 * 28)
    privacies.forEach((info,idx) => {
        const [date, alpha] = info.split(" ")
        const [y, m, d] = date.split(".").map(Number)
        const signDate = d + (m * 28) + (y * 12 * 28)
        
        if (totalDate - signDate >= Type[alpha] * 28) {
            result.push(idx+1)
        }
    })
    
    
    return result;
}