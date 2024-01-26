import sys
input = sys.stdin.readline

def moduler (b, n, mod):
    if n == 0:
        return 1
    x = moduler(b, n // 2, mod)
    if not n % 2:
        return (x * x) % mod
    else :
        return (x * x * b) % mod

N = int(input())
answer = 0
module = 1000000007
for _ in range(N):
    b, a = map(int,input().split())
    re_b = moduler(b, module-2, module)
    answer = (answer + a * re_b ) % module

print(answer)