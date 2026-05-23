# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head_1=l1
        head_2=l2
        dummy=ListNode()
        temp=dummy
        carry=0
        while head_1 and head_2:
            value=(head_1.val + head_2.val + carry)
            remainder=(value)%10
            carry=(value)//10
            dummy.next=ListNode(remainder)
            temp_=dummy.next
            dummy=temp_
            head_1=head_1.next
            head_2=head_2.next
        if head_1:
            while head_1:
                value=head_1.val+carry
                remainder=value%10
                carry=value//10
                dummy.next=ListNode(remainder)
                temp_=dummy.next
                dummy=temp_
                head_1=head_1.next
        else:
            while head_2:
                value=head_2.val+carry
                remainder=value%10
                carry=value//10
                dummy.next=ListNode(remainder)
                temp_=dummy.next
                dummy=temp_
                head_2=head_2.next
        if carry>0:
            dummy.next=ListNode(carry)
            temp_=dummy.next
            dummy=temp_      
        return temp.next

          


        