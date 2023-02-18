N,K = map(int,input().split())
medal = [list(map(int,input().split())) for _ in range(N)]

medal_lst = sorted(medal,key = lambda x : (-x[1],-x[2],-x[3]))
first = [medal_lst[0][1],medal_lst[0][2],medal_lst[0][3]]
rank = 1

for num,G,S,B in medal_lst:
    if first != [G,S,B]:
        rank += 1
    first = [G,S,B]
    if num == K:
        print(rank)
        break