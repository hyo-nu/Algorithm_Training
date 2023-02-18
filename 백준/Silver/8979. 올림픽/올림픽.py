N,con = map(int,input().split())

medal = [list(map(int,input().split())) for _ in range(N)]
rank_dict = {}

for c in range(1,N): # 1,2,3 / 금,은,동
    max = 0

    for r in range(N): # 0 1 2 3
        if max < medal[r][c] : # 첫 메달 갯수 큰놈 찾기
            max = medal[r][c]
            r_idx = r # 그때 선수의 idx
    rank_dict.setdefault(medal[r_idx][0],c) # 딕셔너리 c:등수, medal[][0] : 선수 저장

    for j in range(N):
        if j !=r_idx and max == medal[j][c]: # max랑 동점 비교
            rank_dict.setdefault(medal[j][0],c) # 딕셔너리 {등수 : 선수} 이렇게 추가
        medal[r_idx][j] = 0

print(rank_dict[con])
