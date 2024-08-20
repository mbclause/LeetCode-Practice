"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
corner cases: empty tree, balanced tree?

brute force idea:
traverse tree, keep a depth counter, increment counter as you go down a level, return counter

def maxDepth(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1
    
    depthLeft = traverseTree(root.left, 1)

    depthRight = traverseTree(root.right, 1)

    return max(depthLeft, depthRight)

def traverseTree(node, depth):
    if node == None:
        return depth
    else:
        depthLeft = traverseTree(root.left, depth + 1)

        depthRight = traverseTree(root.right, depth + 1)

        return max(depthLeft, depthRight)

O(n) time
O(1) space
"""

def traverseTree(node, depth):
    if node == None:
        return depth
    else:
        depthLeft = traverseTree(node.left, depth + 1)

        depthRight = traverseTree(node.right, depth + 1)

        return max(depthLeft, depthRight)
    
def maxDepth(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1
    
    depthLeft = traverseTree(root.left, 1)

    depthRight = traverseTree(root.right, 1)

    return max(depthLeft, depthRight)