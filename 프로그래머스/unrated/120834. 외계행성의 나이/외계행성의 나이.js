// a b c d e f g h i j
// 0 1 2 3 4 5 6 7 8 9

function solution(age) {
    const alpha = ["a","b","c","d","e","f","g","h","i","j"]
    const numbers = String(age).split("")
    const newage = numbers.map((number) => {
        return alpha[Number(number)]
    })
    
    return newage.join("")
}