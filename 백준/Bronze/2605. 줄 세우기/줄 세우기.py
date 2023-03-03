N = int(input())
num = list(map(int,input().split()))
lst = []
ST = 1

for i in num:
    if i == 0 : lst.append(ST)
    else : lst.insert(len(lst)-i,ST)
    ST += 1

print(*lst)