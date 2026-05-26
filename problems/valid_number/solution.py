class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits_seen=False
        digits_after_e=True
        e_seen=False
        decimal_seen=False
        for i in range(len(s)):
            if "0"<=s[i]<="9":
                digits_seen=True
                if e_seen:
                    digits_after_e=True
            elif s[i]=="+" or s[i]=="-":
                if i>0 and s[i-1]!="e" and s[i-1]!="E":
                    return False
            elif s[i]=="e" or s[i]=="E":
                if e_seen or not digits_seen:
                    return False
                if i==len(s)-1 or i==0:
                    return False
                e_seen=True
                digits_after_e=False 
            elif s[i]==".":
                if decimal_seen or e_seen:
                    return False
                decimal_seen=True 
            else:
                return False
        return digits_seen and digits_after_e

        
            
            
        