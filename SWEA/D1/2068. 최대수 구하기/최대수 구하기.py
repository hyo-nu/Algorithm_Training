Test = int(input())

for T in range(Test):
    num = list(map(int,input().split()))
    num.sort()
    print(f'#{T+1} {num[len(num)-1]}')