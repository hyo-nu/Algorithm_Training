import sys
input = sys.stdin.readline

def divide_conquer(N):
    if N == 3:
        return ["  *  "," * * ","*****"]
    star = divide_conquer(N // 2)
    t = []
    for i in star:
        t.append(" " * (N//2) + i + " " * (N//2))
    for i in star:
        t.append(i + " " *(N-len(i)) + i)
    return t

N = int(input())
print('\n'.join(divide_conquer(N)))