N = int(input())

tree = {}
for _ in range(N):
    data, left, right = input().strip().split()
    tree[data] = [left, right]
    
def preorder(data):
    if data == ".": return
    print(data, end = "")
    preorder(tree[data][0])
    preorder(tree[data][1])
    
def inorder(data):
    if data == ".": return
    inorder(tree[data][0])
    print(data, end = "")
    inorder(tree[data][1])
    
def postorder(data):
    if data == ".": return
    postorder(tree[data][0])
    postorder(tree[data][1])
    print(data, end = "")

    
preorder('A')
print()
inorder('A')
print()
postorder('A')