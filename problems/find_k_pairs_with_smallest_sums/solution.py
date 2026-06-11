class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k==0 or not nums1 or not nums2:
            return []
        q=[]
        ans=[]
        for i in range(min(k,len(nums1))):
            heapq.heappush(q,(nums1[i]+nums2[0],i,0))
        while q and len(ans)<k:
            sum_,i,j=heapq.heappop(q)
            ans.append([nums1[i],nums2[j]])
            if (j+1)<len(nums2):
                heapq.heappush(q,(nums1[i]+nums2[j+1],i,j+1))
        return ans
            
        