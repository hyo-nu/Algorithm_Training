chess = [1,1,2,2,2,8]
lst = list(map(int,input().split()))
for i in range(len(lst)):
    chess[i] -= lst[i]
print(*chess)