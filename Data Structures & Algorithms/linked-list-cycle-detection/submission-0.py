# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = set()
        temp = head
        while temp is not None:
            vis.add(temp)
            temp = temp.next
            if temp in vis:
                return True
        return False
