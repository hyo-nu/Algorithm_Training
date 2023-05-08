from itertools import combinations

N, S = map(int,input().split())
lst = list(map(int,input().split()))
count = 0

for i in range(1,N+1):
    for p in combinations(lst,i):
        if sum(p) == S : count += 1

print(count)