# 점프 : k 칸 (K)
# 순간이동 : 현재 거리 x 2 (0)

def solution(n):
    value = 1

    while n != 1:
        if n % 2 : value += 1
        n = n // 2
    return value