class Solution(object):
    def countValidSubarrays(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        def check(num,x):
            if num%10!=x:
                return False
            reverse=int(str(abs(num))[::-1])
            if reverse%10!=x:
                return False
            return True            
        n=len(nums)
        prefix_arr=[0]*(n+1)
        for i in range(1,n+1):
            prefix_arr[i]=prefix_arr[i-1]+nums[i-1]
        count=0
        for i in range(n+1):
            for j in range(i+1,n+1):
                sum_=prefix_arr[j]-prefix_arr[i]
                if sum_%10==x:
                    if check(sum_,x):
                        count+=1
        return count
            
                
        
        