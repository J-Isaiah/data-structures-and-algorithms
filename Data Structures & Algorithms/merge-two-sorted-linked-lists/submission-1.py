# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        nl = new_list = ListNode(-1)
        while l1 and l2:
            if l1.val > l2.val:
                nl.next = l2
                l2 = l2.next
            else:
                nl.next = l1
                l1 = l1.next
            nl = nl.next
        
        if l1 and not l2:
            nl.next = l1
        elif l2 and not l1:
            nl.next = l2
        
        return new_list.next





        