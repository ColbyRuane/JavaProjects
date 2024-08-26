# 226. invert binary tree
# given the root of a binary tree, invert the tree, and return its root

# understand:
#   input: 'root' root of a binary tree, type TreeNode
#   output: root of the inverted binary tree, type TreeNode
# constraints: 
#   number of tree nodes [0,100]
#   tree node value [-100,100]           

# approach:
#   when inverting the tree across a vertical axis, parent-child relationships remain
#   the same. if a parent node has a child node, flip its position (left or right)
#   tree.left = tree.right, vice versa
#   pre-order traversal to access root, left and right node of each sub tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder traversal
def printTree(root: TreeNode):
    if root.left:
        printTree(root.left)
    print(root.val, end=' ')
    if root.right:
        printTree(root.right)

def invertTree(root):
    if not root: return
    stack = [root]
    node = TreeNode()

    while stack:
        # pop current node 
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return root
# time-complexity: O(N), corresponding to traversing every node in the tree
# space-complexity: O(h) where h is the height of the tree, corresponding to the maximum 
#   potential size of the stack

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(22)
printTree(root)
print('\n')
printTree(invertTree(root))
     
