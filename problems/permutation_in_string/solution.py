from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1=len(s1)
        map1=Counter(s1)
        i=0
        while i<len(s2)-l1+1:
            str2=s2[i:i+l1]
            map2=Counter(str2)
            if map2==map1:
                return True
            i+=1
        return False
