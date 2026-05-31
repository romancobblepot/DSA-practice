class Solution(object):
    def twoSum(self,nums,start,target):
        mpp={}
        ans=[]
        for i in range(start+1,len(nums)):
            current=nums[i]
            if target-current in mpp:
                ans.append([mpp[target-current],i])
            mpp[current]=i
        return ans
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        target=0
        for i in range(len(nums)):
            current=nums[i]
            needed=self.twoSum(nums,i,target-current)
            if len(needed)!=0:
                for num in needed:
                    j=num[0]
                    k=num[1]
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
        return ans

        