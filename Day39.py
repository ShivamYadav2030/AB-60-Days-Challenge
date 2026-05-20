class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = max_depth(root)
print("Maximum Depth:", result)