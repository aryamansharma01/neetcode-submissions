# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = -math.inf
        def helper(node):
            nonlocal maxval
            if not node:
                return 0
            leftsum = helper(node.left)
            rightsum = helper(node.right)
            maxval = max(maxval, node.val+leftsum + rightsum)
            return max(0,node.val+leftsum,node.val+rightsum)
        helper(root)
        return maxval
            

        