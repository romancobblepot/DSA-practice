class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        map_arr1=set()
        for num in arr1:
            string=str(num)
            for i in range(1,len(string)+1):
                map_arr1.add(string[:i])
        max_length=0
        for num in arr2:
            s=str(num)
            for j in range(1,len(s)+1):
                if s[:j] in map_arr1:
                    max_length=max(max_length,j)
        return max_length


        