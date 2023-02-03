height = 0
bowl = list(input())

for b in range(len(bowl)):
    if b == 0 : height += 10
    elif bowl[b-1] == bowl[b] : height += 5
    elif bowl[b-1] != bowl[b] : height += 10

print(height)