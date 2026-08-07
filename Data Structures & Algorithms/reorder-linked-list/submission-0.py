# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            prev, cur= None, head,
            while cur is not None:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                
            return prev
        
        def find_mid(head):
            fast, slow = head,head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow=slow.next
            return slow

        mid = find_mid(head)
        r_mid = reverse(mid)

        cur = head

        while r_mid.next is not None:
            next_head = cur.next
            nr_mid = r_mid.next

            r_mid.next = next_head
            cur.next = r_mid


            cur = next_head
            r_mid = nr_mid


            
                




        