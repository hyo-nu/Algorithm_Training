N = int(input())
N_lst = list(map(int,input().split()))
 
up_size = []
up_lst = [N_lst[0]]
for n in range(len(N_lst)-1):
 
    if N_lst[n] >= N_lst[n+1]: 
        up_size.append(up_lst[-1]-up_lst[0])
        up_lst.clear()
    up_lst.append(N_lst[n+1])

up_size.append(up_lst[-1]-up_lst[0])
up_size.sort()

print(up_size[-1])