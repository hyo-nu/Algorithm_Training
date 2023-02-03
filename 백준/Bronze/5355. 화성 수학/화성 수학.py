Test = int(input())

for T in range(Test):
    h_s = input().split()
    
    for case in range(1,len(h_s)):
        
        h_s[0] = float(h_s[0])

        if h_s[case] == '@':
            h_s[0] = h_s[0] * 3 
        elif h_s[case] == '%':
            h_s[0] = h_s[0] + 5
        elif h_s[case] == '#':
            h_s[0] = h_s[0] - 7

    print('{:.2f}'.format(round(h_s[0],2)))
