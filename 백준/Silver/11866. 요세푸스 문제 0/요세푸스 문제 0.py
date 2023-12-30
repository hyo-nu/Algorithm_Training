import sys
input = sys.stdin.readline

N, K = map(int,input().split())
lst = [i for i in range(1,N + 1)]

result = []
idx = -1

for _ in range(N):
    idx = (idx + K) % N
    result.append(str(lst.pop(idx)))
    N -= 1; idx -= 1

print("<",', '.join(result),">",sep="")