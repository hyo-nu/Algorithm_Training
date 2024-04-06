import sys;
input = sys.stdin.readline


H, W = map(int,input().split())
blocks = list(map(int,input().split()))

result = 0
for i in range(1, W-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])
    
    compare = min(left_max, right_max)
    
    if blocks[i] < compare:
        result += compare - blocks[i]

print(result)