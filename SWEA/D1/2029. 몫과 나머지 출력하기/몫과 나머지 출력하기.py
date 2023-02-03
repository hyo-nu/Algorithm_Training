Test = int(input())

for T in range(Test):   
    a,b = map(int,input().split())
    print(f'#{T+1} {divmod(a,b)[0]} {divmod(a,b)[1]}')
