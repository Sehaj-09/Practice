class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
def printTree(root):
    if root == None:
        return
    print(root.data, end= ":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        
        print("R", root.right.data, end="")
    print()
    printTree(root.left)
    printTree(root.right)
    
def treeInput():
    rootData=int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def numNodes(root):
    if root==None:
        return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return 1+leftCount+rightCount
root=treeInput()
printTree(root)
print(numNodes(root))
