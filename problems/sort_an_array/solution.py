class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_mapp=defaultdict(int)
        for num in nums:
            hash_mapp[num]+=1
        new_arr=[]
        i=min(nums)
        maxi=max(nums)
        while i<maxi+1:
            actual_num=i
            if actual_num in hash_mapp:
                new_arr.extend([actual_num]*hash_mapp[actual_num])
            i+=1
        return new_arr






        