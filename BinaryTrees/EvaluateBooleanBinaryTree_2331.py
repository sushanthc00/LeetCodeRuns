class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluateBoolTree(root):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return root.val == 1

    left_val = evaluateBoolTree(root.left)
    right_val = evaluateBoolTree(root.right)

    if root.val == 2:
        return left_val or right_val
    elif root.val == 3:
        return left_val and right_val


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    print(evaluateBoolTree(root))
