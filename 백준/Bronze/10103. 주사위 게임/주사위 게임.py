round = int(input())

chang_score = 100
sang_score = 100

for r in range(round):
    chang , sang = map(int,input().split())

    if chang > sang:
        sang_score -=chang
    elif chang < sang:
        chang_score -=sang

print(chang_score)
print(sang_score)

