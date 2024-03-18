import sys;
input = sys.stdin.readline

N, M = map(int,input().split())
pack = 1_000_000
one = 1_000_000
for _ in range(M):
    a , b = map(int,input().split())
    pack = min(pack, a)
    one = min(one, b)

result = 0
if pack < one * 6:
    result = (N // 6) * pack
    if pack > (N % 6) * one:
        print(result + (N % 6) * one)
    else:
        print(result + pack)

else :
    print( one * N)