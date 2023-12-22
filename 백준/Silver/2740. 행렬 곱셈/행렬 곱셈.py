import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(N)]

M, K = map(int,input().split())
arr2 = [list(map(int,input().split())) for _ in range(M)]

result = [[sum([a * b for a, b in zip(lst1,lst2)]) for lst2 in list(zip(*arr2)) ] for lst1 in arr1]

for lst in result:
    print(*lst)