class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp=defaultdict(int)
        max_len=1
        prev=0
        for i in range(len(arr)):
                if arr[i]-difference in dp:
                    dp[arr[i]]=dp[arr[i]-difference]+1
                    max_len=max(max_len,dp[arr[i]])
                else:
                    dp[arr[i]]=1
        return max_len
            
        
        