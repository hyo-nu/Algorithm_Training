import sys;
input = sys.stdin.readline

n, m = map(int,input().split())
books = sorted(list(map(int,input().split())))
sp, ep = 0, len(books) - 1
distance = []

while True:
    if -books[sp] >= books[ep] and books[sp] < 0:
        for i in range(m):
            if sp + i < n and books[sp + i] > 0 : i -= 1 ; break
        distance.append(-books[sp])
        sp += (i + 1)
    elif -books[sp] < books[ep] and books[ep] > 0:
        for i in range(m):
            if ep - i >= 0 and books[ep - i] < 0: i -= 1 ; break
        distance.append(books[ep])
        ep -= (i + 1)

    if sp > ep : break

print(sum (map(lambda x : x * 2 ,distance)) - distance[0])