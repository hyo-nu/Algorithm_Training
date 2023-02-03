# 조합 아이디어

Test = int(input())

def mul(lst):
    ans = 1
    for m in lst:
        if m != 0 : ans *= m
        else : return 0
    return ans

for T in range(Test):
    N, M = map(int,input().split())

    if N > M: 
       up_lst = [a for a in range(1,N+1)] # 분자
       down_lst1 = [b for b in range(1,N-M+1)] # 분모1
       down_lst2 = [c for c in range(1,M+1)] # 분모2

    elif N < M:
       up_lst = [a for a in range(1,M+1)] # 분자
       down_lst1 = [b for b in range(1,M-N+1)] # 분모1
       down_lst2 = [c for c in range(1,N+1)] # 분모2
    
    elif N == M:
        print('1')
        continue

    bridge_cnt = mul(up_lst)/mul(down_lst1)/mul(down_lst2)
    print(round(bridge_cnt))
