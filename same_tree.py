"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

constraints:
    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

    

corner cases: can have empty tree, values are same but different structure, structure is same but values different

Brute Force:
    Idea: Iterate through both trees, first check if values are same, then check if they have a left child, 
    then check if they have right child. Traverse to next node and repeat. Return false if any of these checks fail
    Return true if we reach the end.
"""

class Solution(object):
    # recursive function to iterate through each node of both trees
    def sameTreeRecurse(self, nodeP, nodeQ):
        # base cases
        # if one of the nodes is null
        if nodeP == None or nodeQ == None:
            # if both aren't null, return false
            if not(nodeP == None and nodeQ == None):
                return False
            else:
                return True

        # check if nodes have same value, if not, False
        if nodeP.val != nodeQ.val:
            return False

        # check left children
        resultLeft = self.sameTreeRecurse(nodeP.left, nodeQ.left)

        # check right children
        resultRight = self.sameTreeRecurse(nodeP.right, nodeQ.right)

        if resultLeft and resultRight:
            return True
        else:
            return False



    def isSameTree(self, p, q):
        return self.sameTreeRecurse(p, q)