import sys;
input = sys.stdin.readline

def isPrime(n):
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0 : return 0
    return 1

n = int(input())
stack = []
case = sp = Sum = 0
num = 2

while True:
    if num <= n:
        if isPrime(num):
            stack.append(num)
            Sum += num
        num += 1

    while Sum >= n :
        if Sum == n : case += 1
        Sum -= stack[sp]
        sp += 1

    if Sum < n and num > n : break

print(case)