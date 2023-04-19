N = int(input())
N_lst = list(map(int,input().split()))
sset = set()
for key in N_lst : sset.add(key)
lst = sorted(list(sset))
dic = {lst[i] : i for i in range(len(lst))}
for i in range(N):
    print(dic[N_lst[i]],end=' ')