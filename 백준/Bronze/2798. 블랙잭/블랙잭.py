
N, M = map(int,input().split())
nums = list(map(int,input().split()))

# nums = [5,6,7,8,9]
# n = 5

lst = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            # print([i,j,k]) 
            lst.append([i,j,k])
           
max_lst = []
for l in lst:
    sum = 0
    for o in l : sum += nums[o]
    if sum <= M : max_lst.append(sum)

max_lst.sort()        
print(max_lst[-1])