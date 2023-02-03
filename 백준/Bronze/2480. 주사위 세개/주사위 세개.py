dice_num = list(map(int,input().split()))

def MAX(dice):
    max = dice[0]
    for c in range(len(dice)-1):
        if dice[c] <= dice(c+1):
            max = dice[c]
    return max

def same(dice):
    for c in range(len(dice)-1):
        for d in range(c+1,len(dice)):   
            if dice[c] == dice[d]:
                result = dice[c]
    return result

count = 0
for c in range(len(dice_num)-1):
    for d in range(c+1,len(dice_num)):
        if dice_num[c] == dice_num[d]:
            count += 1

if count == 3: #3개 동일
    print(10000 + same(dice_num) * 1000)
elif count == 1: #2개 동일
    print(1000 + same(dice_num) * 100)
elif count == 0: #다 다름
    print(max(dice_num) * 100)

