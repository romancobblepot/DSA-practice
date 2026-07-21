class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        s='1'+s+'1'
        last_seen_zero=[-1]*(len(s))
        next_seen_zero=[len(s)]*len(s)
        last_seen_one=[0]*(len(s))
        next_seen_one=[len(s)-1]*len(s)
        last_val_zero=-1
        next_val_zero=len(s)
        last_val_one=0
        next_val_one=len(s)-1
        no_ones=0
        for i in range(len(s)):
            last_seen_zero[i]=last_val_zero
            last_seen_one[i]=last_val_one
            if s[i]=='0':
                last_val_zero=i
            elif s[i]=='1':
                no_ones+=1
                last_val_one=i
        for i in range(len(s)-1,0,-1):
            next_seen_zero[i]=next_val_zero
            next_seen_one[i]=next_val_one
            if s[i]=='0':
                next_val_zero=i
            elif s[i]=='1':
                next_val_one=i
        maxi=0
        for i in range(1,len(s)-1):
            if s[i]=='1':
                next_zero=next_seen_zero[i]
                last_zero=last_seen_zero[i]
                if next_zero==len(s) or last_zero==-1:
                    maxi=max(maxi,no_ones-2)
                    continue
                last_one=last_seen_one[last_zero]
                next_one=next_seen_one[next_zero]
                maxi=max(maxi,next_one-next_zero-last_one+last_zero+no_ones-2)
        return maxi



        




        