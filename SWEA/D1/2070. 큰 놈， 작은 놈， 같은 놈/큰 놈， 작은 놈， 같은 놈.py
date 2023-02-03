Test = int(input())

for T in range(Test):
    a,b = map(int,input().split())
    
    if a > b : print(f"#{T+1} >")
    elif a < b : print(f"#{T+1} <")
    elif a == b : print(f"#{T+1} =")