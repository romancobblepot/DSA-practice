import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr=[]
        for i in range(len(nums)):
            if i<k:
                heapq.heappush(arr,nums[i])
            else:
                if nums[i]>arr[0]:
                    heapq.heappop(arr)
                    heapq.heappush(arr,nums[i])
        return arr[0]



        