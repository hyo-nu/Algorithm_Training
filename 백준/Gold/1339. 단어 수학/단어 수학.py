import sys;
input = sys.stdin.readline

n = int(input())
numbers = [input().rstrip() for _ in range(n)]
alpha = { chr(i+65) : 0 for i in range(26)}

for i in range(n):
    length = len(numbers[i])
    for j in range(length):
        alpha[numbers[i][j]] += 10**(length-j-1)

alpha = sorted(alpha.items(), key = lambda x : -x[1])
setnumber = 9
result = 0
for key, value in alpha:
    if value == 0 : break
    result += value * setnumber
    setnumber -= 1

print(result)