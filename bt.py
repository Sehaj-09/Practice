class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
def printTree(root):
    if root == None:
        return
    print(root.data, end= ":")
    print("L", root.data.left, end=",")
    print("R", root.data.right)
    printTree(root.left)
    printTree(root.right)
    
btn1=Node(1)
btn2=Node(2)
btn3=Node(3)

btn1.left=btn2
btn1.right=btn3
printTree(btn1)
    
