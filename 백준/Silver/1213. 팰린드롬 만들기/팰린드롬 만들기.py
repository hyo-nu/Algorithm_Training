import sys;
input = sys.stdin.readline


alpha = [0] * 26
for s in input().rstrip() : alpha[ord(s)-65] += 1

forward = ""
back = ""
one = ""
for i in range(26):
    if alpha[i] % 2 == 0:
        forward += chr(i + 65) * (alpha[i] // 2)
        back += chr(i + 65) * (alpha[i] // 2)
    elif alpha[i] % 2 == 1 and not one:
        if alpha[i] > 1 :
            forward += chr(i + 65) * (alpha[i] // 2)
            back += chr(i + 65) * (alpha[i] // 2)
        one += chr(i + 65)
    else:
        forward = back = one = ""
        break
if not forward and not back and not one:
    print("I'm Sorry Hansoo")
else:
    print(forward + one + back[::-1])