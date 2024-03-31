# col번째 컴럼의 값 기준으로 오름차순
# 값이 동일하면, 첫번째 컬럼의 값 기준으로 내림차순
# i 번째 행의 컴럼값을 i로 나눈 나머지의 합

def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x :(x[col-1], -x[0]))
    hashValue = 0
    
    for row in range(row_begin-1, row_end):
        for col in range(len(data[row])):
            hashValue += (data[row][col] % (row + 1))
        
    return hashValue

