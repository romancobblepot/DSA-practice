class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrack(idx,s,arr,ans):
            if idx>len(s)-1:
                ans.append(arr[:])
                return
            for i in range(idx,len(s)):
                s1=s[idx:i+1]
                if s1==s1[::-1]:               
                    arr.append(s1)
                    backtrack(i+1,s,arr,ans)
                    arr.pop()         
        ans=[]
        arr=[]
        backtrack(0,s,arr,ans)
        return ans
            

        