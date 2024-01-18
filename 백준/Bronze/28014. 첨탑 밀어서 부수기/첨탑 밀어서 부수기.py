N = int(input())
lst = list(map(int,input().split()))
count = 1

for i in range(N-1,0,-1):
    if lst[i] >= lst[i-1] : count += 1

print(count)