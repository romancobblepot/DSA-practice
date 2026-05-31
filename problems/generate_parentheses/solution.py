class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open_count=1
        closed_count=0
        def backtrack(ans,count,arr,open_count,closed_count):
            if count<=0 and open_count==closed_count:
                arr.append(ans)
                return
            if open_count<n:
                backtrack(ans+'(',count-1,arr,open_count+1,closed_count)
            if open_count>closed_count:
                backtrack(ans+')',count-1,arr,open_count,closed_count+1)
            return arr
        arr=[]
        return backtrack('(',2*n-1,arr,open_count,closed_count)

        