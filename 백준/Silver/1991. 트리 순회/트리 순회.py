import sys
input = sys.stdin.readline

N = int(input())
G = {}
preorder = inorder  = postorder = ""
for _ in range(N):
    root, left, right = input().split()
    G[root] = (left, right)

def Back(node):
    global preorder, inorder, postorder
    if node == ".":
        return
    preorder += node
    Back(G[node][0])
    inorder += node
    Back(G[node][1])
    postorder += node

Back("A")
print(preorder)
print(inorder)
print(postorder)