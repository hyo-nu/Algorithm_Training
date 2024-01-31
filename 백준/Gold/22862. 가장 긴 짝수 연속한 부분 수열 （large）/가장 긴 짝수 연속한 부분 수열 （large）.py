import sys
input = sys.stdin.readline

N, K = map(int,input().split())
lst = list(map(int,input().split()))

sp = ep = delete = length = length_max = 0

while ep < N:
    if not lst[ep] % 2 :  # 짝수라면
        ep += 1
        length += 1
        length_max = max(length_max, length)

    elif lst[ep] % 2 :  # 홀수라면
        delete += 1
        ep += 1

        while delete > K:
            if lst[sp] % 2 :
                delete -= 1
                sp += 1
            elif not lst[sp] % 2:
                sp += 1
                length -= 1

print(length_max)