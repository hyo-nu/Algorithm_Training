def K_count(puzzle,N,K):
    K_cnt = 0
    puzzle_lst =''.join(puzzle).split('0')
    for i in range(len(puzzle_lst)):
        if len(puzzle_lst[i]) == K:
            K_cnt +=1
    return K_cnt         

Test = int(input())

for T in range(Test):
    N,K = map(int,input().split()) # 5 3 
    K_cnt = 0
    row_dict = {}
    
    for i in range(N):
        puzzle = list(map(str,input().split())) 
        # 가로 확인하기
        K_cnt += K_count(puzzle,N,K)
          
        # 세로를 딕셔너리로 만들기
        for k in range(N):
            if k not in row_dict : row_dict[k] = [puzzle[k]]
            else : row_dict[k] += [puzzle[k]]
    
    #세로 확인하기
    for l in range(N):
        K_cnt += K_count(row_dict[l],N,K)
        
    print(f'#{T+1} {K_cnt}')