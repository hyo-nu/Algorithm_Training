// a b c d e f g h i j
// 0 1 2 3 4 5 6 7 8 9

function solution(age) {
    return age.toString().split("").map((number) => {return "abcdefghij"[number]}).join("")
}