import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.total=sum(w)
        self.arr=[]
        start=0
        for i in range(len(w)):
            start+=w[i]
            self.arr.append(start)
    def pickIndex(self):
        """
        :rtype: int
        """
        index=random.randint(1,self.total)
        low=0
        high=len(self.arr)-1
        while low<=high:
            mid=(low+high)//2
            if self.arr[mid]>=index:
                high=mid-1
            else:
                low=mid+1
        return low


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()