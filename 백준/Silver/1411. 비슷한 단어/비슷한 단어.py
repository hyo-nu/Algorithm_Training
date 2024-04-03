import sys;
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i+1,N):
        alpha = ["0"] * 26
        for k in range(len(words[i])):
            if alpha[ord(words[i][k])-97] == "0" and words[j][k] not in alpha:
                alpha[ord(words[i][k])-97] = words[j][k]

            elif alpha[ord(words[i][k])-97] != words[j][k]:
                break
        else:
            count+=1
print(count)