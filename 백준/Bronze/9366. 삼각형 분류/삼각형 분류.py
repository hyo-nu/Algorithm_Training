for case in range(1, int(input()) + 1):
    result = ""
    a, b, c = list(map(int,input().split()))
    if a+b <= c or a+c <= b or b+c <=a : result = "invalid!"
    elif  a == b and b == c : result = "equilateral"
    elif a == b or b == c or a == c : result = "isosceles"
    else : result = "scalene"
    print(f'Case #{case}: {result}')