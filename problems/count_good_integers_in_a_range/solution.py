class Solution(object):
    def goodIntegers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        def count_upto(N,k):
            digits=list(map(int,str(N)))
            m=len(digits)
            dp=[[[[[0]*2 for _ in range(2)] for _ in range(k+1)] for _ in range(11)]for _ in range(m+1)]        #dp[pos][diff][tight][started]
            dp[0][10][0][1][0]=1
            for pos in range(m):
                for prev in range(11):
                    for diff in range(k+1):
                        for tight in range(2):
                            for started in range(2):
                                curr=dp[pos][prev][diff][tight][started]
                                if curr==0:
                                    continue
                                limit=digits[pos] if tight else 9
                                for d in range(limit+1):
                                    ntight=tight and (d==limit)
                                    if started==0 and d==0:
                                        dp[pos+1][10][0][ntight][0]+=curr
                                        continue
                                    if started==0:
                                        dp[pos+1][d][0][ntight][1]+=curr
                                        continue
                                    if abs(d-prev)<=k:
                                        dp[pos+1][d][d-prev][ntight][1]+=curr
                                    else:
                                        continue
            ans=0
            for prev in range(11):
                for diff in range(k+1):
                    for tight in range(2):
                        for started in range(2):
                            ans+=dp[m][prev][diff][tight][started]
            return ans
        return count_upto(r,k)-count_upto(l-1,k)

                                


        
        