# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def remove_tail(self,head):
        temp=head
        prev=None
        while temp.next:
            prev=temp
            temp=temp.next
        prev.next=None
        temp.next=head
        return temp
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        node=head
        count=0
        if not head:
            return None
        if not head.next:
            return head
        if k==0:
            return head
        length=0
        while node:
            length+=1
            node=node.next
        temp=head
        while count<(k%length):
            new_head=self.remove_tail(temp)
            temp=new_head
            count+=1
        return temp



        