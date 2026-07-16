class Solution(object):
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd=[]
        maxi=0
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            prefixGcd.append(self.gcd(maxi,nums[i]))
        prefixGcd.sort()
        l=0
        r=len(nums)-1
        total=0
        while l<r:
            total+=self.gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return total

        