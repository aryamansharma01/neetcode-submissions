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
            curr = node.val+max(0,leftsum) + max(0,rightsum)
            maxval = max(maxval, curr)
            return node.val+max(0,leftsum,rightsum)
        helper(root)
        return maxval
            

        