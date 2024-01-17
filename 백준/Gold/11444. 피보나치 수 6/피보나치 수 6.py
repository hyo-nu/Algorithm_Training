import sys
input = sys.stdin.readline

N = int(input())
matrix = [(1,1),(1,0)]

def power(matrix, exp):
    if exp <= 1 :
        return [(1,1),(1,0)]
    else :
        x = power(matrix, exp // 2)
        sub = [[sum([a*b for a,b in zip(lst1, lst2)]) % 1000000007 for lst2 in list(zip(*x))] for lst1 in x]
        if exp % 2 == 0:
            return sub
        else:
            return [[sum([a*b for a,b in zip(lst1, lst2)]) % 1000000007 for lst2 in list(zip(*sub))] for lst1 in matrix]

print(power(matrix, N - 1)[0][0])