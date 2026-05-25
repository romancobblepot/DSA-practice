# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def split(self,head):
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=None
        return slow
    def merge(self,l1,l2):
        dummy=ListNode()
        temp=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1:
            dummy.next=l1
        else:
            dummy.next=l2
        return temp.next
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        left=head
        right=self.split(head)
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)       