Test = int(input())

Y_score = 0
K_score = 0

for T in range(Test):
    for c in range(9):
        Y,K = map(int,input().split())
        
        Y_score += Y
        K_score += K

    if Y_score > K_score:
        print("Yonsei")
    elif Y_score < K_score:
        print("Korea")
    elif Y_score == K_score:
        print("Draw")