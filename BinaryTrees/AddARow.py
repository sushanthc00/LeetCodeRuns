class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(root, val, depth):
    if depth == 1:
        return Treenode(val, left=root)

    def addRow(node, curr_depth):
        if not node:
            return

        if curr_depth == depth - 1:
            node.left = Treenode(val, left=node.left)
            node.right = Treenode(val, right=node.right)

        else:
            addRow(node.left, curr_depth + 1)
            addRow(node.right, curr_depth + 1)

    addRow(root, 1)

    return root


if __name__ == '__main__':
    root = [4, 2, 6, 3, 1, 5]
    val = 1
    depth = 2

    print(addOneRow(root, val, depth))