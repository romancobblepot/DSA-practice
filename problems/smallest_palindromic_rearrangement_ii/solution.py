from collections import Counter,OrderedDict
class Solution(object):
    def count_factorial(self,new_mapp,n,k):
        ways=1
        remaining=n
        for char,values in new_mapp.items():
            if values==0:
                continue
            y=1
            for j in range(1,values+1):
                y=y*(remaining-values+j)//j
                if y>=k:
                    y=k
                    break
            ways*=y
            if ways>=k:
                return k
            remaining-=values
        return ways
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)==1:
            return s
        end=len(s)//2 -1
        mapp=Counter(s[:end+1])
        new_mapp=OrderedDict(sorted(mapp.items()))
        ans=""
        n=end+1
        if self.count_factorial(new_mapp,n,k)<k:
            return ""
        key_arr=new_mapp.keys()
        n_total=n
        for _ in range(n_total):
            for char in key_arr:
                if new_mapp[char]==0:
                    continue
                else:
                    n-=1
                    new_mapp[char]-=1 
                    count=self.count_factorial(new_mapp,n,k)               
                    if count>=k:
                        ans+=char
                        break       
                    else:
                        k-=count
                        n+=1
                        new_mapp[char]+=1 
        if len(s)%2==0:
            return ans+ans[::-1]
        else:
            return ans+s[end+1]+ans[::-1]
        


        