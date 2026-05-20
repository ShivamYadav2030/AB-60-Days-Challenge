class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

result = inorder_traversal(root)

print("Inorder Traversal:", result)