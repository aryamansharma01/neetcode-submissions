# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if root is None:
            return []
        q.append(root)
        while q:
            n = len(q)
            level = []
            for i in range(n):
                ele = q.popleft()
                if ele:
                    level.append(ele.val)
                    q.append(ele.left)
                    q.append(ele.right)
            if level:
                res.append(level)
        return res