# 3*2 2*3
# 3*3 3*3 

def solution(arr1, arr2):
    # print(*arr1)
    # print(list(zip(*arr1)))    
    # for lst in arr1:
    #     print(lst)
    # print("======")
    # for lst in  list(zip(*arr2)):
    #     print(lst)
    
    arr1 = arr1
    arr2 = list(zip(*arr2))
    arr = []
    for lst1 in arr1:
        value = []
        for lst2 in arr2:
            value.append(sum([a * b for a, b in zip(lst1,lst2)]))
        arr.append(value)
    return arr
    
# import numpy as np

# def solution(arr1, arr2):
#     arr1 = np.array(arr1)
#     arr2 = np.array(arr2)
#     return (arr1 @ arr2).tolist()