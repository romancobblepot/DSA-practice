class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        mapp=defaultdict(int)
        for l in s:
            if l==x or l==y:
                mapp[l]+=1
        ans=""
        count_y=mapp[y]
        count_x=mapp[x]
        for i in range(count_y):
            ans+=y
        for i in range(count_x):
            ans+=x
        for l in s:
            if l!=x and l!=y:
                ans+=l
        return ans
        