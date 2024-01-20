S = input()
new = ""
for i in range(len(S)):
    if S[i] != S[i].upper() : new += S[i].upper()
    else : new += S[i].lower()
print(new)
