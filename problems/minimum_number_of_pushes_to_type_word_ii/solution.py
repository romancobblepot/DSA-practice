from collections import Counter,OrderedDict
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        i=1
        n=len(word)
        total=0
        max_value=2
        count=1
        mapp={}
        freq=Counter(word)
        sorted_freq=OrderedDict(sorted(freq.items(), key=lambda x:x[1],reverse=True))
        for char in sorted_freq:
            if char not in mapp:
                if max_value==10:
                    max_value=2
                    count+=1
                mapp[char]=count
                max_value+=1
        for char in word:
            total+=mapp[char]
        return total

            

