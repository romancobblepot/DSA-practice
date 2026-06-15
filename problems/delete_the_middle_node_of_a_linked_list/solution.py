# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_left=None
        middle=head
        right=head
        if not head.next:
            return None
        while right and right.next:
            right=right.next.next
            new_left=middle
            middle=middle.next
        new_right=middle.next
        new_left.next=new_right
        return head


        