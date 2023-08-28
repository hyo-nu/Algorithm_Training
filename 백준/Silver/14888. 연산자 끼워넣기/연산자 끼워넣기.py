def back(n,Sum):
    global Min,Max
    if n == N:
        Min = min(Min,Sum)
        Max = max(Max,Sum)
        return
    for i in range(len(calcul)):
        if not vi[i]:
            vi[i] = 1
            if calcul[i] == 0: back(n+1,Sum + nums[n])
            if calcul[i] == 1: back(n+1,Sum - nums[n])
            if calcul[i] == 2: back(n+1,Sum * nums[n])
            if calcul[i] == 3:
                if Sum >= 0 : back(n+1,Sum // nums[n])
                else : back(n + 1, -(abs(Sum) // nums[n]))
            vi[i] = 0

N = int(input())
nums = list(map(int,input().split()))
signs = list(map(int,input().split()))
calcul = []
for idx, sign in enumerate(signs):
    tmp = [idx] * sign
    calcul += tmp
Max, Min = -1000000001, 1000000001
vi = [0] * len(calcul)
back(1,nums[0])
print(Max)
print(Min)