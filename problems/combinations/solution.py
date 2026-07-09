class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(idx,ans,arr,l):
            if l==k:
                ans.append(arr[:])
                return 
            for i in range(idx+1,n+1):
                arr.append(i)
                dfs(i,ans,arr,l+1)
                arr.pop()
        ans=[]
        dfs(0,ans,[],0)
        return ans






        