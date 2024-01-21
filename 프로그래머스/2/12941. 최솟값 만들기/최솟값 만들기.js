function solution(A,B){
    A = A.sort((a,b) => a-b)
    B = B.sort((a,b) => b-a)
    var answer = 0;
    
    A.forEach((num,idx)=>{
        answer += A[idx] * B[idx]
    })

    return answer;
}