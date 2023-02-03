T = int(input())

for c in range(0,T):
    numbers = list(map(int,input().split()))
    avg = sum(numbers) / 10
    print(f'#{c+1} {round(avg)}')   
