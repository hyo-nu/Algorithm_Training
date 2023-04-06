import sys
input = sys.stdin.readline

NM_set = []
N_set = set()
N, M = map(int,input().split())

for _ in range(N):
    N_set.add(input().rstrip())

for _ in range(M):
    m = input().rstrip()
    if m in N_set : NM_set.append(m)

NM_set.sort()
print(len(NM_set))
for i in NM_set:print(i)