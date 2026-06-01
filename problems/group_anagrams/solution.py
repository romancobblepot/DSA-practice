from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapp=defaultdict(list)
        for i in range(len(strs)):
            word=strs[i]
            sorted_word=str(sorted(word))
            if sorted_word in mapp:
                mapp[sorted_word].append(word)
            else:
                mapp[sorted_word]=[word]
        return list(mapp.values())




        