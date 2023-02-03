T = int(input())

result=[]

for c in range(0,T):
    l = list(map(int,input().split()))
    l.sort()
    result.append(l)

for d in range(0,T):
    print("#" + str(d+1),result[d][9])




