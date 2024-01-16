import sys
input = sys.stdin.readline

N, B = map(int,input().split())
matrix = [list(map(lambda x: int(x) % 1000,input().split())) for _ in range(N)]

def power(matrix, exp):
    if exp == 1:
        return matrix
    else:
        x = power(matrix,exp // 2)
        sub = [[sum([a*b for a,b in zip(x1,x2)]) % 1000 for x2 in list(zip(*x))] for x1 in x]
        if exp % 2 == 0:
            return sub
        else :
            return [[sum([a*b for a,b in zip(x1,x2)]) % 1000 for x2 in list(zip(*sub))] for x1 in matrix]

for lst in power(matrix,B) : print(*lst)