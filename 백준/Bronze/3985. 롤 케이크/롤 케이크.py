# L미터의 롤 케이크
# N명에게 배분
# P ~ K 번 조각
L = int(input())
N = int(input())
G = [0] * (L + 1)
Max = 0
Max_R = 0
for i in range(1,N+1):
    P, K = map(int,input().split())
    if Max < K-P :
        Max , idx = K-P , i

    cnt = 0
    for j in range(P,K+1):
        if G[j] == 0:
            G[j] = i
            cnt += 1
    if Max_R < cnt :
        Max_R, idx_R = cnt , i

print(idx)
print(idx_R)