Test = int(input())

for T in range(Test):
    P,Q,R,S,W = map(int,input().split())
    
    A_company = P*W
    if W > R : B_company = Q + S*(W-R)
    else : B_company = Q
    
    if A_company < B_company : print(f'#{T+1} {A_company}')
    else : print(f'#{T+1} {B_company}')
    
