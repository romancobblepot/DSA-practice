class Solution(object):
    def createGrid(self, m, n):
        ans=""
        res=[]
        for i in range(n):
            ans+="."
        res.append(ans)
        for i in range(1,m):
            ans=""
            for j in range(n-1):
                ans+="#"
            ans+="."
            res.append(ans)
        return res
                




            

            
        