n,m = map(int,input().split())

result = 1
for i in range(n,n-m,-1):
    result = result * i // (n+1-i)
print(result)
