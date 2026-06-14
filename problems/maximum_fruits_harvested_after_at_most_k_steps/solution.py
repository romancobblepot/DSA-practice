class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        left=0
        total=0
        max_count=float('-inf')
        for i in range(len(fruits)):
            right=fruits[i][0]
            total+=fruits[i][1]
            while left<=i and min(abs(startPos-fruits[left][0])+right-fruits[left][0],abs(right-startPos)+right-fruits[left][0])>k:
                total-=fruits[left][1]
                left+=1
            max_count=max(max_count,total)
        return max_count



        