class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapp=defaultdict(int)
        for w in s:
            mapp[w]+=1
        q=[]
        for key in mapp:
            heapq.heappush(q,(-mapp[key],key))
        last_used="#"
        ans=""
        while len(q)>1:
            _,character1=heapq.heappop(q)
            _,character2=heapq.heappop(q)
            ans+=character1+character2
            mapp[character1]-=1
            mapp[character2]-=1
            if mapp[character1]>0:
                heapq.heappush(q,(-mapp[character1],character1))
            if mapp[character2]>0:
                 heapq.heappush(q,(-mapp[character2],character2))
        if q:
            _,char=heapq.heappop(q)
            ans+=char
        if len(ans)!=len(s):
            return ""
        return ans


        