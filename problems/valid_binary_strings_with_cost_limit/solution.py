class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        ans=[]
        def backtrack(idx,ans,current,cost,prev_one):
            if cost>k:
                return
            if idx==n:
                ans.append("".join(current[:]))
                return
            current.append("0")
            backtrack(idx+1,ans,current,cost,False)
            current.pop()
            if not prev_one:
                current.append("1")
                backtrack(idx+1,ans,current,cost+idx,True)
                current.pop()
        backtrack(0,ans,[],0,False)
        return ans
            
            
            