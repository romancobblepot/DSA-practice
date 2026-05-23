# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        pq=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(pq,(node.val,i,node))
        dummy=ListNode()
        temp=dummy
        while pq:
            _,i,smallest=heapq.heappop(pq)
            dummy.next=smallest
            if smallest.next:
                smallest=smallest.next
                heapq.heappush(pq,(smallest.val,i,smallest))
            dummy=dummy.next
        return temp.next
        