# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        points_arr=[]
        ans=[-1,-1]
        prev=head
        curr=head.next
        ahead=head.next.next
        idx=0
        while ahead:
            if curr.val<ahead.val and curr.val<prev.val:
                points_arr.append(idx)
            elif curr.val>ahead.val and curr.val>prev.val:
                points_arr.append(idx)
            idx+=1
            ahead=ahead.next
            prev=prev.next
            curr=curr.next
        if len(points_arr)<2:
            return ans
        ans[0]=float('inf')
        for i in range(1,len(points_arr)):
            ans[0]=min(ans[0],points_arr[i]-points_arr[i-1])
        ans[1]=points_arr[-1]-points_arr[0]
        return ans

                
        