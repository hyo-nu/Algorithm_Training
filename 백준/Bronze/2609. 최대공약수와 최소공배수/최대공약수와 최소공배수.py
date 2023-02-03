def maxnum(a,b):
    for i in range(max(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return i
            break

def minnum(a,b):
    for i in range(max(a,b),(a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
            break


a,b = map(int,input().split())

print(maxnum(a,b))
print(minnum(a,b))