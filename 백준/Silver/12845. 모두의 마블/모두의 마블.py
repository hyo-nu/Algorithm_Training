N = int(input())
lst = list(map(int,input().split()))

for i in range(N):
    if lst[i] == max(lst): MP = i ; break

print(sum(lst) + lst[MP] * (N-2))