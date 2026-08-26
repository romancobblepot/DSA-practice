class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=0
        r=k
        n=len(s)
        ones=0
        idx=defaultdict(list)
        min_length=n
        for i in range(k):
            if s[i]=='1':
                ones+=1
        if ones==k:
            idx[k].append(s[:k])
            min_length=k
        while r<n:
            if s[r]=='1':
                ones+=1
            while ones>=k:
                if ones==k:
                    idx[r-l+1].append(s[l:r+1])
                    min_length=min(min_length,r-l+1)
                if s[l]=='1':
                    ones-=1
                l+=1
            r+=1
        indices=idx[min_length]
        indices.sort()
        return indices[0] if indices else ""

        





        