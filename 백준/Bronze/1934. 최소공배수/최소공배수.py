Test = int(input())

def factorization(num): # 소인수분해
    result_lst = []
    for c in range(2,num+1):
        while num % c == 0:
            num = num // c
            result_lst.append(c)
    return result_lst

for T in range(Test):
    a, b = map(int,input().split())
    
    # a의 소인수분해 요소 list
    a_dict = {}
    for a in factorization(a):
        if str(a) in a_dict:
            a_dict[str(a)] = a_dict[str(a)] + 1
        else:
            a_dict[str(a)] = 1

    # b의 소인수분해 요소 list
    b_dict = {}
    for b in factorization(b):
        if str(b) in b_dict:
            b_dict[str(b)] = b_dict[str(b)] + 1
        else:
            b_dict[str(b)] = 1  
    
    ab_dict = dict(b_dict, **a_dict) # b_dict에 a_dict요소 덮어쓴 딕셔너리 형성 
    mul_dict = {}

    for c in ab_dict:
        if ab_dict[c] not in mul_dict:
            mul_dict[c] = ab_dict[c] 
        for d in b_dict:
            if c == d:
                if ab_dict[c] > b_dict[d]:
                    mul_dict[c] = ab_dict[c]
                elif ab_dict[c] < b_dict[d]:
                    mul_dict[c] = b_dict[c]
    sum = 1
    for c in mul_dict:
        sum *= int(c)**mul_dict[c]
    print(sum)

