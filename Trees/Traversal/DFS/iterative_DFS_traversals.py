class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        
def preorder_traversal(root):
    if root is None:
        return
    stack=[]
    stack.append(root)
    while len(stack)>0:
        node = stack.pop()
        print(node.value)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
            
def inorder_traversal(root):
    if root is None:
        return
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            if len(stack)==0:
                break
            node=stack.pop()
            print(node.value)
            if node.right is not None:
                stack.append(node.right)
            
def postorder_traversal(root):
    if root is None:
        return
    stack1=[]
    stack2=[]
    stack1.append(root)
    while len(stack1)>0:
        node=stack1.pop()
        stack2.append(node)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
    while len(stack2)>0:
        print(stack2.pop().value)
            
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(9)
root.right.left = Node(5)
root.right.right = Node(6)

print("Preorder traversal:")
preorder_traversal(root)
print("Inorder traversal:")
inorder_traversal(root)
print("Postorder traversal:")
postorder_traversal(root)
