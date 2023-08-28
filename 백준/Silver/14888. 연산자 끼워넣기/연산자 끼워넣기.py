a=int(input())
b=list(map(int, input().split()))
add, sub, mul, div=map(int, input().split())
maxi,mini=-1000000000,1000000000
ans=0
def cal(add, sub, mul, div, ans, i):
    global maxi, mini
    if i==a:
        if ans>=maxi:
            maxi=ans
        if ans<=mini:
            mini=ans
        return
    if add>0:
        cal(add-1, sub, mul, div, ans+b[i], i+1)
    if sub>0:
        cal(add, sub-1, mul, div, ans-b[i], i+1)
    if mul>0:
        cal(add, sub, mul-1, div, ans*b[i], i+1)
    if div>0:
        cal(add, sub, mul, div-1, int(ans/b[i]), i+1)
cal(add, sub, mul, div, b[0], 1)
print(maxi)
print(mini)