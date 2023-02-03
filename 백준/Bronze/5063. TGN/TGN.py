Test = int(input())

for c in range(Test):
    r,e,c = map(int,input().split())

    if r > e-c:
        print("do not advertise")
    elif r == e-c:
        print("does not matter")
    elif r < e-c:
        print("advertise")