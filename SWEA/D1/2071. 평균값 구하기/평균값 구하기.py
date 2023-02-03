T = int(input())

result=[]

for c in range(0,T):
    l = sum(list(map(int,input().split())))
    average = round(l/10)

    result.append(average)

for d in range(0,T):
    print("#" + str(d+1),result[d])
