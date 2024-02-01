import sys
input = sys.stdin.readline

# S이상 중, 가장 짧은 길이

N, S = map(int,input().split())
lst = list(map(int,input().split()))

sp = ep = cur_sum = 0
length_min = 100000

while ep < N :
    while ep < N and cur_sum < S:
        cur_sum += lst[ep]
        ep += 1

    while cur_sum >= S :
        length_min = min(length_min, ep - sp)
        cur_sum -= lst[sp]
        sp += 1

print(length_min if length_min != 100000 else 0)