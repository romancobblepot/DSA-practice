class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1] + nums[i-1]
        hash_=defaultdict(int)
        count=0
        for i in range(len(prefix)):
            prefix[i]=prefix[i]%k
            if prefix[i] in hash_:
                count+=hash_[prefix[i]]
            hash_[prefix[i]]+=1
        return count
        


            


        