# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth):
            if node is None:
                return 0
            d_left = d_right = depth
            if node.left:
                d_left = helper(node.left,depth+1)
            if node.right:
                d_right = helper(node.right, depth+1)
            return max(d_left,d_right)
        return helper(root,1)
        