# 2 <= len(numbers) <= 20
# 1 <= numbers <= 50
# 1 <= target <= 1000

def back(n,result,num,target):
    
    if n == len(num)-2:
        if result == target:
            num[len(num)-1] += 1
        return
    back(n+1,result + num[n+1],num,target)
    back(n+1,result - num[n+1],num,target)

def solution(numbers, target):
    num = [0] + numbers +[0]
    back(0,0,num,target)
    return num[len(num)-1]