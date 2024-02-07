import sys;
from collections import deque
input = sys.stdin.readline

def palindrome(sp, ep, delete):
    Min = 10
    while sp < ep:
        if word[sp] == word[ep]:
            sp += 1 ; ep -= 1

        else:
            if delete : return 2
            if word[sp+1] == word[ep]: Min = min(Min,palindrome(sp+1,ep,1))
            if word[sp] == word[ep-1]: Min = min(Min,palindrome(sp,ep-1,1))
            if word[sp+1] != word[ep] and word[sp] != word[ep-1]: return 2
            break

    if delete : return 1
    if Min == 10 : return 0
    else : return Min

for _ in range(int(input())):
    word = input().rstrip()
    sp, ep = 0, len(word) - 1
    print(palindrome(sp,ep,0))