class Solution(object):
    def twoSum(self,nums,start,target):
        mapp=defaultdict(int)
        ans=[]
        for i in range(start,len(nums)):
            if target-nums[i] in mapp:
                ans.append([nums[i],target-nums[i]])
            mapp[nums[i]]+=1
        return ans
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=set()
        n=len(nums)
        for i in range(n):
            target=-nums[i]
            two_sum=self.twoSum(nums,i+1,target)
            for u,v in two_sum:
                triple=tuple(sorted((nums[i],u,v)))
                ans.add(triple)
        output=list(list(i) for i in ans)
        return output





        