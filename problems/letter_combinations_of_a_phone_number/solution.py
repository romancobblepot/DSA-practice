import string
from collections import defaultdict
from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n=len(digits)
        mapp=defaultdict(list)
        start=2
        count=0
        for ch in string.ascii_lowercase:
            if start>6:
                break
            if count<3:
                mapp[start].append(ch)
                count+=1
                if count==3:
                    count=0
                    start+=1
        mapp[start]=list("pqrs")
        mapp[8]=list("tuv")
        mapp[9]=list("wxyz")
        arr=[]
        for num in digits:
            arr.append(mapp[int(num)])
        ans=[''.join(p) for p in product(*arr)]
        return ans
        



        