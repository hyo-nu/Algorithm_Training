arr = [0]*10
num = input()

for i in num:
    if int(i) == 6 or int(i) == 9 : arr[6] +=1
    else : arr[int(i)] += 1

if arr[6] % 2 == 0 : arr[6] = arr[6]//2
else : arr[6] = arr[6]//2 + 1

max = 0
for i in range(len(arr)):
    if max < arr[i] :
        max = arr[i]
        number = i

else : print(max)