# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        len=0
        node=head
        while node:
            node=node.next
            len+=1
        steps=len-n
        if steps==0:
            return head.next
        prev=None
        temp=head
        for i in range(steps):
            prev=temp
            temp=temp.next
        if temp.next:
            new_tail=temp.next
        else:
            new_tail=None
        prev.next=new_tail
        return head 

        