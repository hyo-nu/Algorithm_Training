arr = [[0]*100 for _ in range(100)]
sum = 0

for _ in range(4):
    R,C,X,Y = map(int,input().split())

    for i in range(R,X):
        for j in range(C,Y):
            arr[i][j] += 1
            if arr[i][j] == 1:
                sum += 1
print(sum)