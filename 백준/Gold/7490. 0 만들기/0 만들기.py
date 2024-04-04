import sys;
input = sys.stdin.readline

def back(n,s):
    if n >= N :
        Sum = 0
        tmp = ""
        for i in s.replace(" ","")[::-1]:
            if i.isdigit() : tmp = i + tmp
            else :
                if i == "+":
                    Sum += int(tmp) ; tmp = ""
                elif i == "-":
                    Sum -= int(tmp) ; tmp = ""
        Sum += int(tmp)
        if Sum == 0 : print(s)
        return

    back(n+1,s + " " + str(n+1))
    back(n+1,s + "+" + str(n+1))
    back(n+1,s + "-" + str(n+1))

for _ in range(int(input())):
    N = int(input())
    back(1,"1")
    print()