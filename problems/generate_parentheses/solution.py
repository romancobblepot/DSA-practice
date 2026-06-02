class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open_count=1
        string="("
        closed_count=0
        def backtrack(open_count,closed_count,n,ans,string):
            if n==0 and open_count==closed_count:
                ans.append(string)
                return 
            if closed_count>open_count or n<0:
                return
            backtrack(open_count+1,closed_count,n-1,ans,string+'(')
            if closed_count<open_count:
                backtrack(open_count,closed_count+1,n-1,ans,string+')')
        ans=[]
        backtrack(open_count,closed_count,(2*n)-1,ans,string)
        return ans


        