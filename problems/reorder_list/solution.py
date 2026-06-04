# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLL(self,head):
        prev=None
        temp=head
        while temp:
            node=temp.next
            temp.next=prev
            prev=temp            
            temp=node
        return prev
    def merge(self,head_1,head_2,main_head):
        old_next_1=head_1.next
        old_next_2=head_2.next
        if main_head:
            main_head.next=head_1
            main_head=main_head.next
            main_head.next=head_2
            main_head=main_head.next
        else:
            main_head=head_1
            main_head.next=head_2
            main_head=main_head.next
        return main_head,old_next_1,old_next_2
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        node=head
        temp=head
        if not node.next:
            return node
        def Split(node):
            slow=node
            fast=node
            while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            split_head=slow.next
            slow.next=None
            return split_head
        split_head=Split(temp)
        new_split_head=self.reverseLL(split_head)
        temp_2=new_split_head
        temp_1=head
        main_head=None
        dummy=main_head
        while temp_1 and temp_2:
            new_head,old_1,old_2=self.merge(temp_1,temp_2,main_head)
            main_head=new_head
            temp_1=old_1
            temp_2=old_2
        if temp_1:
            main_head.next=temp_1
        if temp_2:
            main_head.next=temp_2
        return head


        