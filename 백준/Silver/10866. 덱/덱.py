import sys
from collections import deque

input = sys.stdin.readline

lst = deque()
for _ in range(int(input())):
    value = input().split()

    if value[0] == "push_front" : lst.appendleft(value[1])
    elif value[0] == "push_back": lst.append(value[1])
    elif value[0] == "pop_front": print(lst.popleft()) if lst else print(-1)
    elif value[0] == "pop_back": print(lst.pop()) if lst else print(-1)
    elif value[0] == "front": print(lst[0]) if lst else print(-1)
    elif value[0] == "back": print(lst[-1]) if lst else print(-1)
    elif value[0] == "size": print(len(lst))
    elif value[0] == "empty": print(0) if lst else print(1)