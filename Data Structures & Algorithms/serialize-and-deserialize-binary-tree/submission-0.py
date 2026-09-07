# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res= ""
        while q:
            ele = q.popleft()
            if ele is not None:
                res+=str(ele.val)+","
                q.append(ele.left)
                q.append(ele.right)
            else:
                res+="#,"
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data =="#,":
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))

        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i]=="#":
                node.left = None
            else:
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            if vals[i+1]=="#":
                node.right = None
            else:
                node.right = TreeNode(int(vals[i+1]))
                q.append(node.right)
            i+=2
        return root
            
            

        

            
            
