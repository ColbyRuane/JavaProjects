# 104. maximu depth of binary tree
# given the root of a binary tree, return its maximum depth
# max depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node

# understand:
#   input: 'root' root of binary tree, type TreeNode (implmentation below)
#   output: integer maximum depth
# constraints:
#   number of nodes [0, 10^4]
#   node value [-100, 100]

# approach:
#   global count of depth during traversal of binary tree
#   recursive depth-first search 

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root) -> int:
    # size of tree edge cases
    if root is None: return 0

    # add 1 for root node 
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
# time-complexity: O(N), corresponding to traversal of every node in the tree
# space-complexity: O(N), corresponding to depth of the recursion stack,
#   best case O(logN) for balanced tree, O(N) for skewed tree at worst
