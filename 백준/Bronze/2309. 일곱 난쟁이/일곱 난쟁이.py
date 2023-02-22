def back(n,lst,sum):
    if n > 8:
        if len(lst) == 7 and sum == 100:
            ans.append(lst)
        return
    back(n+1,lst + [seven[n]],sum + seven[n])
    back(n+1,lst,sum)

seven = [int(input()) for _ in range(9)]
ans = []
back(0,[],0)
result = sorted(ans[0])

for i in result:
    print(i)