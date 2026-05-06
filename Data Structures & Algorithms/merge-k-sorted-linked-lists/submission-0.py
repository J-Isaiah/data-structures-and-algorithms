# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge_helper(lists)
    
    def merge_helper(self,lists):
        place_holder = None

        for i in range(len(lists)):
            place_holder = self.merge(place_holder, lists[i])
        return place_holder


        





    def merge(self,l1,l2):
        first_node = placeHolder = ListNode()
        first = l1
        second = l2
        while first and second:
            if  first.val >= second.val:
                placeHolder.next = second
                second = second.next
                placeHolder = placeHolder.next
            else: 
                placeHolder.next = first
                first = first.next
                placeHolder = placeHolder.next
        
        if first is not None:
            placeHolder.next = first
        if second is not None:
            placeHolder.next = second
        return first_node.next
        
            




        