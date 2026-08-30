class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_ch=defaultdict(int)
        for ch in s:
            freq_ch[ch]+=1
        freq_set=set()
        count=0
        for ch in freq_ch.keys():
            while freq_ch[ch] in freq_set and freq_ch[ch]>0:
                freq_ch[ch]-=1
                count+=1
            freq_set.add(freq_ch[ch])
        return count


        