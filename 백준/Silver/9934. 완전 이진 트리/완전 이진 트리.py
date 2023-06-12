def binary(level,middle,total):
    if level == K:
        return
    tree[level].append(middle)
    binary(level+1, middle - ((total // 2) + 1),total//2)
    binary(level+1, middle + ((total // 2) + 1),total//2)

K = int(input())
nodes = list(map(int,input().split()))
middle = (2**K-1)//2
tree = [[] for _  in range(K)]
binary(0,middle,middle)
for lst in tree:
    for i in range(len(lst)):
        print(nodes[lst[i]],end=" ")
    print()