Test = int(input())

for T in range(Test):
    num = int(input())
    sum = 0
    for n in range(1,num+1):
        if n % 2 != 0 : sum += n
        elif n % 2 == 0 : sum -= n
    print(f'#{T+1} {sum}')