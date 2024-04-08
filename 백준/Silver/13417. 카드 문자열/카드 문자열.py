import sys;
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = list(map(str,input().split()))
    result = ""

    for s in lst:
        if not result : result += s ; continue
        if ord(result[0]) >= ord(s) : result = s + result
        else : result += s

    print(result)