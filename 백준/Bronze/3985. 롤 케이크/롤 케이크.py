L = int(input())
N = int(input())
result1 = 0
max_lst = [0] * (L+1)
max_val = 0
max_val2 = 0
result1 = 0
result2 = 0
for i in range(1, N+1):
    P, K = list(map(int, input().split()))
    if max_val2 < K-P:
        max_val2 = K-P
        result1 = i
    for j in range(P, K+1):
        if max_lst[j] == 0:
            max_lst[j] = i
print(result1)
for i in range(1, N+1):
    if max_val < max_lst.count(i):
        max_val = max_lst.count(i)
        result2 = i
print(result2)