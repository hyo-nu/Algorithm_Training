// 대문자 -> 소문자
// 소문자, 숫자, -, _, . 빼고 제거
// . 2번 이상이면 . 으로
// . 처음 or 끝에 있으면 제거
// 빈 문자열이면 a 대입
// 16자 이상이면 15개로 축약 제거 후 끝에 . 있으면 제거
// id 2자 이하면, 길이가 3이 될때까지 마지막 문자 반복

function solution(new_id) {
    const pattern = /[a-zA-Z0-9_.-]/
    new_id = new_id.toLowerCase()
    console.log("1단계",new_id)
    
    new_id = new_id.split("").filter((value) => {
        return value,pattern.test(value) ? value : ""
    })
    console.log("2단계",new_id.join(""))
    
    new_id = new_id.join('')
    while (new_id.includes("..")){
        new_id = new_id.replaceAll("..",".")
    }
    console.log("3단계",new_id)
    
    if (new_id[0] === ".") {new_id = new_id.slice(1)}
    if (new_id[new_id.length-1] === ".") {
        new_id = new_id.slice(0,-1)}
   
    console.log("4단계",new_id)

    if (new_id === ""){ new_id = "a" }
    console.log(new_id)
    
    console.log("5단계",new_id)
    
    
    if (new_id.length >= 16) {
        new_id = new_id.slice(0,15)
        if (new_id[14] === "."){
            new_id = new_id.slice(0,-1)
        }
    }
    console.log("6단계",new_id)

    
    while(new_id.length <= 2){
        new_id += new_id[new_id.length-1]
    }

    console.log("7단계",new_id)

    
    return new_id;
}