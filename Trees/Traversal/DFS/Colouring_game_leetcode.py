def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def find_node(root, x):
            stack=[]
            stack.append(root)
            while stack:
                node=stack.pop()
                if node.val==x:
                    return node
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        def size_tree(root):
            count=1
            stack=[]
            stack.append(root)
            while stack:
                node=stack.pop()
                if node.val==x:
                    return node
                if node.left:
                    stack.append(node.left)
                    count+=1
                if node.right:
                    stack.append(node.right)
                    count+=1
            return count

        a,b,c=0,0,0
        if root.val==x:
            a=size_tree(root.left)
            b=size_tree(root.right)
            c=0
        else:
            node=find_node(root,x)
            if node.left:
                b=size_tree(node.left)
            if node.right:
                c=size_tree(node.right)
            a=n-b-c-1
        if a>=n/2 or b>=n/2 or c>=n/2:
            return True
        return False

# Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# Output: true
