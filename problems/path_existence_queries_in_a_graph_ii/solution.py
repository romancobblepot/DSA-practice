class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        arr=[]
        for i,num in enumerate(nums):
            arr.append((num,i))
        pos={}
        arr.sort()
        for sorted_index,(_,original_index) in enumerate(arr):
            pos[original_index]=sorted_index
        values=[num for num,_ in arr]
        r=0
        max_right=[0]*n
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            max_right[l] = r
        LOG=(n).bit_length()
        up=[[-1]*LOG for _ in range(n)]
        for i in range(n):
            up[i][0]=max_right[i]
        for j in range(LOG-1):
            for i in range(n):
                if up[i][j]!=-1:
                    up[i][j+1]=up[up[i][j]][j]
        ans=[]
        for u,v in queries:
            u = pos[u]
            v = pos[v]
            if u>v:
                u,v=v,u
            total=0
            if u==v:
                ans.append(total)
                continue
            curr=u
            for j in range(LOG-1,-1,-1):
                if up[curr][j]!=curr and up[curr][j]<v:
                    curr=up[curr][j]
                    total+= 1<<j
            if up[curr][0]!=curr and up[curr][0]>=v:
                total+=1
            else:
                total=-1
            ans.append(total)
        return ans
            
        




        



        