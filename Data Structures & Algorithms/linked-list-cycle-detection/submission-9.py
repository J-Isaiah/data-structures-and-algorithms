# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast !=  slow :
            if fast == None or fast.next == None:
                return False   

            fast = fast.next.next
            slow = slow.next
        return True

        
        