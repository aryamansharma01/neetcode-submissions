# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxsofar):
            if not node:
                return 0
            res = 1 if node.val>=maxsofar else 0
            maxsofar = max(maxsofar, node.val)
            res+=helper(node.left,maxsofar)
            res+=helper(node.right,maxsofar)
            return res
        return helper(root,root.val)
        
        

        