class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini=min(nums)
        maxi=max(nums)
        mapp=set()
        for num in nums:
            mapp.add(num)
        ans=[]
        for i in range(mini,maxi+1):
            if i not in mapp:
                ans.append(i)
        return ans
