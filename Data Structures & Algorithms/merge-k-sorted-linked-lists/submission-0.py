# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(list1,list2):
            dummy = node = ListNode()
            while list1 and list2:
                if list1.val<list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2= list2.next
                node = node.next
            node.next = list1 or list2
            return dummy.next
        def solve(lists):
            if len(lists)==0:
                return None
            if len(lists)==1:
                return lists[0]
            mid = len(lists)//2
            left = solve(lists[:mid])
            right = solve(lists[mid:])
            return merge2(left,right)
        return solve(lists)
        