from collections import deque

N, M = map(int,input().split())
nums = list(map(int,input().split()))

Q = deque()
for i in range(N):
    Q.append(i+1)

cnt = 0
while nums:
    p = nums.pop(0)
    posi = 0
    for i in range(len(Q)):
        if p == Q[i]:
            break
        posi += 1

    while p != Q[0]:
        # 왼쪽꺼 순환
        if posi <= len(Q)/2:
            out = Q.popleft()
            Q.append(out)
            cnt += 1
        # 오른쪽꺼 순환
        else:
            out = Q.pop()
            Q.appendleft(out)
            cnt += 1

    Q.popleft()

print(cnt)