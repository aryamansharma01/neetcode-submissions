# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, minval, maxval):
            if not node:
                return True
            if node.val>=maxval or node.val<=minval:
                return False

            return helper(node.left,minval,node.val) and helper(node.right,node.val,maxval)
        return helper(root,-math.inf,math.inf)