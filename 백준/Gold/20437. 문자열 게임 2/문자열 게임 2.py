Test = int(input())

for TC in range(Test):
    W = input()
    K = int(input())
    alpa = {chr(i) : [] for i in range(97,123)}
    for i in range(len(W)):
        alpa[W[i]].append(i)
    Max = 0
    Min = len(W) + 1
    for lst in alpa.values():
        if len(lst) >= K:
            for i in range(len(lst)-K + 1):
                if Min > lst[i+K-1] - lst[i] + 1: Min = lst[i+K-1] - lst[i] + 1
                if Max < lst[i+K-1] - lst[i] + 1: Max = lst[i+K-1] - lst[i] + 1

    if Max == 0 and Min == len(W) + 1:
        print(-1)
    else:
        print(Min,Max)