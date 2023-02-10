Test = int(input())

for T in range(Test):
    N = int(input())
    words = ''
    for i in range(N):
        word,num = input().split()
        words += word*int(num)
    
    jump = 0
    print(f'#{T+1}')
    for j in words:
        jump += 1
        print(j,end = '')
        if jump % 10 == 0 : print()
    print()    
        
    