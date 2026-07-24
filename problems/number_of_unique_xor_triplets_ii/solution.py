
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=list(set(nums))
        num_set=set()
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                    first=nums1[i]^nums1[j]
                    num_set.add(first)
        num_final=set(list(nums1[:]))
        num_array=list(num_set)
        for num in num_array:
            for k in range(len(nums1)):
                num_final.add(num^nums1[k])
        return len(num_final)
                    



        