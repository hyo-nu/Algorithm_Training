import sys;
input = sys.stdin.readline

N, M = map(int,input().split())
S = {}
for _ in range(N):
    word = input()
    S[word] = 1

cnt = 0
for _ in range(M):
    word = input()
    if word in S : cnt+=1
print(cnt)