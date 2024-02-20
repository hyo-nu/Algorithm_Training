import sys;
input = sys.stdin.readline

def find(sp):
    if parents[sp] != sp:
        parents[sp] = find(parents[sp])
    return parents[sp]

def union(sp, ep):
    parents[find(sp)] = find(ep)

def change(num):
    if num >= 97 : return num - 96
    elif num >= 65 : return num - 38
    elif num == 48 : return 53

n = int(input())
lines = [list(input().rstrip()) for _ in range(n)]
parents = list(range(n))
G = []
total = 0

for r in range(n):
    for c in range(r + 1, n):
        if lines[r][c] == "0" and lines[c][r] == "0" : continue
        num1 = change(ord(lines[r][c]))
        num2 = change(ord(lines[c][r]))
        G.append((r,c,min(num1,num2)))
        if num1 == 53 : num1 = 0
        if num2 == 53 : num2 = 0
        total += num1 + num2

for r in range(n):
    if lines[r][r] == "0": continue
    total += change(ord(lines[r][r]))

G.sort(key = lambda x:x[2])

Min = edge = 0
for sp, ep, weight in G:
    if find(sp) != find(ep):
        Min += weight
        edge += 1
        union(sp, ep)
        if edge == n-1:
            break

print(total-Min if edge == n-1 else -1)