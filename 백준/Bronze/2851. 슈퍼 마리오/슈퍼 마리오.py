num_lst = []
for i in range(10):
    num = int(input())    
    num_lst.append(num)
    
sum = 0
for n in num_lst:
    sum += n
    after = sum - 100 # 100보다 큼
    before = 100 - (sum-n) #100보다 작음
    
    if sum >= 100:
        if after > before : 
            sum =sum-n 
        else :
            sum = sum 
        break
print(sum)
