function solution(food) {
    let left = "", right = ""
    
    food.forEach((cnt, kcal) => {
        left = left + String(kcal).repeat(Math.floor(cnt/2))
        right = String(kcal).repeat(Math.floor(cnt/2)) + right
    })
    return `${left}0${right}`
}