import math
c, a, b = map(int,input().split())
z = ((c**2) / ((b**2) + (a**2))) ** (1/2)
h, w = math.floor(a * z), math.floor(b * z)
print(h,w)