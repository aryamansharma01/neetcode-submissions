# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res= []
        q.append(root)
        while q:
            n= len(q)
            for i in range(n):
                ele = q.popleft()
                if ele:
                    if i==n-1:
                        res.append(ele.val)
                    if ele.left:
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)
        return res


        