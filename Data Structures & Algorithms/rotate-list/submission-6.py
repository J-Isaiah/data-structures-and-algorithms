# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 

        if not head.next:
            return head
            
        cur = head
        num_nodes = 1
        result = None
        while cur.next:
            num_nodes +=1
            cur = cur.next

        cur.next = head 

        rotate = num_nodes - (k%num_nodes)-1
        
        cur = head

        while rotate:
            rotate -=1
            prev = cur
            cur = cur.next

        result = cur.next
        cur.next = None

        return result 


        