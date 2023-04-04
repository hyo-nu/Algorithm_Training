M, N = map(int,input().split())

for a in range(M,N+1):
    for i in range(1,int(a**(1/2))+1):
        if i > 1 and a % i == 0:
            break
    else:
        if a != 1:print(a)
