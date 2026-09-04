# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node is None:
                return
            temp = None
            if node.left:
                temp = node.left
            node.left = node.right
            node.right = temp
            if node.right:
                helper(node.right)
            if node.left:
                helper(node.left)
        helper(root)
        return root
        