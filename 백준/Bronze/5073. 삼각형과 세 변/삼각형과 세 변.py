while(True):
    a, b, c = list(map(int,input().split()))
    if a == 0  and b == 0 and c == 0 : break
    if a == b and b == c: 
        print("Equilateral")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    elif a != b and b != c and a != c :
        print("Scalene")
    else:
        print("Isosceles")
        