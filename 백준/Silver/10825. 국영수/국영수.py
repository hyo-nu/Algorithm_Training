import sys
input = sys.stdin.readline
for name,_,_,_ in sorted([tuple(input().split()) for _ in range(int(input()))],key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0])):print(name)