class Solution(object):
    def NGE(self,arr):
        ans=[-1]*len(arr)
        greatest=-1
        n=len(arr)
        for i in range(n-1,-1,-1):
            current_element=arr[i]
            if greatest<=current_element:
                greatest=current_element
            else:
                ans[i]=greatest
        return ans
    def PGE(self,arr):
        greatest=-1
        i=0
        n=len(arr)
        ans=[-1]*n
        for i in range(n):
            if arr[i]>=greatest:
                greatest=arr[i]
            else:
                ans[i]=greatest
        return ans
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        PreviousGreatestElement=self.PGE(height)
        NextGreaterElement=self.NGE(height)
        n=len(height)
        sum=0
        for i in range(n):
            if PreviousGreatestElement[i]==-1 or NextGreaterElement[i]==-1:
                continue
            else:
                sum+=(min(NextGreaterElement[i],PreviousGreatestElement[i])-height[i])
        return sum
        