import sys 
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    cloth = {}
    for _ in range(n):
        name, kind = input().split()
        cloth[kind] = cloth.get(kind,0) + 1

    case = 1
    for _, value in cloth.items():
        case *= (value + 1)

    print(case-1)