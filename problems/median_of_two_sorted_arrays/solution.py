class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        low=0
        n=len(nums1)
        m=len(nums2)
        if len(nums1)>len(nums2):
            n=len(nums2)
            m=len(nums1)
            nums1,nums2=nums2,nums1
        high=n
        left_size=(n+m+1)//2
        while low<=high:
            mid=low+(high-low)//2
            if mid<=0:
                l1=float('-inf')
            else:
                l1=nums1[mid-1]
            if mid>=n:
                r1=float('inf')
            else:
                r1=nums1[mid]
            partition_right=left_size-mid
            if partition_right==0:
                l2=float('-inf')
            else:
                l2=nums2[partition_right-1]
            if partition_right==m:
                r2=float('inf')
            else:
                r2=nums2[partition_right]
            if l1>r2:
                high=mid-1
            elif l2>r1:
                low=mid+1
            else:
                if (n+m)%2!=0:
                    return max(l1,l2)
                else:
                    return (max(l1,l2) + min(r1,r2))/2.0

        