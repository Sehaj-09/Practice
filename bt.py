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
def largestData(root):
    if root==None:
        return -1
    leftLargest=largestData(root.left)
    rightLargest=largestData(root.right)
    ans=max(leftLargest,rightLargest,root.data)
    return ans 
def numLeafNodes(root):
    if root==None:
        return 0
    if root.left==None and root.right == None:
        return 1
    numLL=numLeafNodes(root.left)
    numLR=numLeafNodes(root.right)
    return numLL+numLR

def numNodes(root):
    if root==None:
        return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return 1+leftCount+rightCount

def printDepthK(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k-1)
    printDepthK(root.right, k-1)

def printDepthKV2(root, k, d=0):
    if root == None:
        return
    if k==d:
        print(root.data)
        return
    printDepthKV2(root.left, k, d+1)
    printDepthKV2(root.right, k, d+1)
root=treeInput()
printTree(root)
print(largestData(root))
print(numLeafNodes(root))
printDepthK(root, 2)
printDepthKV2(root, 2)
