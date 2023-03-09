def solution(n, arr1, arr2):
    Map = [[' '] * n for _ in range(n)]
    answer = []
    
    for i in range(n):
        tmp = ''
        Bin1 = list(bin(arr1[i])[2:])
        Bin2 = list(bin(arr2[i])[2:])
        
        for j in range(len(Bin1)-1,-1,-1):
            if Bin1[j] == '1':Map[i][len(Bin1)-1-j] = '#'
        
        for j in range(len(Bin2)-1,-1,-1):
            if Bin2[j] == '1':Map[i][len(Bin2)-1-j] = '#'
        
        for j in range(n-1,-1,-1):
            tmp += Map[i][j]
        answer.append(tmp)
    return answer

# n = 5
# arr1 = [9,20,28,18,11]
# arr2 = [30,1,21,17,28]

# print(solution(n,arr1,arr2))