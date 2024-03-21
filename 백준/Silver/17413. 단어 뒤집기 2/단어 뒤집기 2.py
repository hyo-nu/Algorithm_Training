import sys;
input = sys.stdin.readline

words = input()
stack = []
sp = 0
while True:
    openPos = words[sp:].find("<")
    tmp = []
    if openPos == -1:
        for word in words[sp:].split():
            tmp.append("".join(list(word)[::-1]))
        stack.append(" ".join(tmp))
        break

    for word in words[sp : sp + openPos].split():
        tmp.append("".join(list(word)[::-1]))
    stack.append(" ".join(tmp))
    sp = sp + openPos

    closePos = words[sp:].find(">")
    stack.append(words[sp : sp + closePos + 1])
    sp = sp + closePos + 1

print("".join(stack))