import sys
input = sys.stdin.readline
N,K = map(int,input().split())
DP = [[0,[]] for _ in range(K+1)]
WV_lst =[]

for i in range(N):
    W,V = map(int,input().split())
    WV_lst.append((W,V))
    if W <= K and DP[W][0] < V:
        DP[W][0] = V
        if DP[W][1]:
            DP[W][1] = [i]
        else:
            DP[W][1].append(i)

for j in range(len(DP)):
    for idx, WV in enumerate(WV_lst):
        w, v = WV[0], WV[1]
        if DP[j][0] != 0 and j + w <= K and idx not in DP[j][1]:
            if DP[j+w][0] < DP[j][0] + v:
                DP[j+w][0] = DP[j][0] + v
                DP[j+w][1] = DP[j][1]+[idx]
print(max(DP,key = lambda x : x[0])[0])