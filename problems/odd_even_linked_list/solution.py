# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        even_head=head
        odd_head=head.next
        temp=odd_head
        while odd_head and odd_head.next:
            even_head.next=odd_head.next
            even_head=even_head.next
            odd_head.next=odd_head.next.next
            odd_head=odd_head.next
        even_head.next=temp        
        return head
        