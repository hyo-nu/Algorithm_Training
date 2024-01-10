function solution(numbers, hand) {
    let answer = '';
    const keypad = {
        1 : [1,1], 2 : [1,2], 3 : [1,3],
        4 : [2,1], 5 : [2,2], 6 : [2,3],
        7 : [3,1], 8 : [3,2], 9 : [3,3],
        "*" : [4,1], 0 : [4,2], "#" : [4,3],
    }
    let lSpot = keypad["*"], rSpot = keypad["#"] 
    numbers.forEach((num,idx) => {
        if ([1,4,7].includes(num)) {
            lSpot = keypad[num]
            answer += "L"
        }
        else if ([3,6,9].includes(num)) {
            rSpot = keypad[num]
            answer += "R"
        }
        else if ([2,5,8,0].includes(num)) {
            const lDistance = Math.abs(keypad[num][0] - lSpot[0]) +  Math.abs(keypad[num][1] - lSpot[1])
            const RDistance = Math.abs(keypad[num][0] - rSpot[0]) +  Math.abs(keypad[num][1] - rSpot[1])
            const Distance = lDistance - RDistance
            if (Distance < 0){ 
                lSpot = keypad[num]
                answer += "L"     
            }
            else if (Distance > 0){
                rSpot = keypad[num]
                answer += "R"
            }
            else {
                if (hand === "left"){
                    lSpot = keypad[num]
                    answer += "L" 
                }
                else if (hand === "right"){
                    rSpot = keypad[num]
                    answer += "R"
                }
            }
        }
    })
    
    return answer;
}