import sys

input = sys.stdin.readline

deque = []
for _ in range(int(input())):
    value = input().split()

    if value[0] == "push_front" :
        deque.insert(0,value[1])
    elif value[0] == "push_back":
        deque.append(value[1])
    elif value[0] == "pop_front":
        print(deque.pop(0)) if deque else print(-1)
    elif value[0] == "pop_back":
        print(deque.pop()) if deque else print(-1)
    elif value[0] == "front":
        print(deque[0]) if deque else print(-1)
    elif value[0] == "back":
        print(deque[-1]) if deque else print(-1)
    elif value[0] == "size":
        print(len(deque))
    elif value[0] == "empty":
        print(0) if deque else print(1)