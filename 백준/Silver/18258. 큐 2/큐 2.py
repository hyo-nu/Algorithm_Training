import sys;
from collections import deque
input = sys.stdin.readline

Q = deque([])
for _ in range(int(input())):
    say, *num = input().split()
    if say == "push" : Q.append(int(num[0]))
    elif say == "pop":
        if Q : print(Q.popleft())
        else : print(-1)
    elif say == "size" : print(len(Q))
    elif say == "empty" :
        if Q : print(0)
        else : print(1)
    elif say == "front" :
        if Q : print(Q[0])
        else : print(-1)
    elif say == "back" :
        if Q : print(Q[-1])
        else : print(-1)