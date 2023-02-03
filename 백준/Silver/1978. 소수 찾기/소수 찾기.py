

N = int(input())
nums = list(map(int,input().split()))

decimal_cnt = 0
for ns in nums:
    count = 0

    for n in range(1,ns+1):
        if ns % n == 0:
            count += 1
    if count == 2:
        decimal_cnt += 1

print(decimal_cnt)

