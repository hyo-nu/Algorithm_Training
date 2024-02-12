import sys;
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
count = {}
score = [0] * N

for i in range(N):
    count[nums[i]] = i

for i in range(N):
    num = nums[i]
    divisor = set([1])
    for j in range(2, int(num ** (1/2)) + 1):
        if num % j == 0:
            divisor.add(j) ; divisor.add(num//j)

    for el in divisor:
        if el in count:
            score[i] -= 1
            score[count[el]] += 1

print(*score)