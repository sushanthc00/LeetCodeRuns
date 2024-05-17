class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/

def deleteLeaves(root, target):
    if not root:
        return None

    root.left = deleteLeaves(root.left, target)
    root.right = deleteLeaves(root.right, target)

    if not root.left and not root.right and root.val == target:
        return None

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)

    target = 2
    root = deleteLeaves(root, target)
    inorder(root)
