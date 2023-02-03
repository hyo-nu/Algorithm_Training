Test = int(input())

for T in range(Test):
    N = int(input())
    num = list(map(int,input().split()))
    num.sort()

    print(f'#{T+1}', end =' ')
    for n in num:
        print(n, end = ' ')
    print()
