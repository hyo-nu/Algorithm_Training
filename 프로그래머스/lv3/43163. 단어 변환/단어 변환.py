from collections import deque

def solution(begin, target, words):
    Q = deque()
    Q.append((begin,0))
    vi = [0] * (len(words) + 1)
    vi[0] = 1
    
    def BFS():
        while Q:
            begin, point = Q.popleft()
            for idx, word in enumerate(words,1):
                if not vi[idx]:
                    cnt = 0
                    for i in range(len(word)):
                        if begin[i] != word[i]:cnt += 1
                        if cnt > 1: break
                    else:
                        vi[idx] = vi[point] + 1
                        Q.append((word,idx))
    
    for idx, word in enumerate(words):
        if target == word : target = idx
    if str(target).isdigit():
        BFS()
        
        return vi[target+1]-1    
    else:
        return 0
    
