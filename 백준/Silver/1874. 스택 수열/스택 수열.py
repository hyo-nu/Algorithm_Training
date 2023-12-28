import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
stack, calcul = [], []

def sequence():
    idx = 0
    for n in range(1, N + 1):
        if lst[idx] >= n :
            stack.append(n)
            calcul.append('+\n')

        while idx < N and lst[idx] <= n :
            if stack.pop() != lst[idx] : return False
            calcul.append('-\n')
            idx += 1
    return True

print("".join(calcul)) if sequence() else print("NO")
