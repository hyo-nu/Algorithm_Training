import sys;
input = sys.stdin.readline

a,b,c = int(input()),int(input()),int(input())
total_angle = a + b + c
if total_angle == 180:
    if a == b and b == c :
        print("Equilateral")
    elif a == c or b == c or a == b:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")