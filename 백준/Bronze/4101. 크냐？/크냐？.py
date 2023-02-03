B, S = map(int,input().split())

while B > 0 or S > 0:
    if B > S:
        print("Yes")
    else:
        print('No')
    B, S = map(int,input().split())

