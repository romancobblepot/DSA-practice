class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        arr=[1]*n
        for i in range(n-1,0,-1):
            if ratings[i]>ratings[i-1]:
                arr[i]=max(arr[i-1]+1,arr[i])
            elif ratings[i-1]>ratings[i]:
                arr[i-1]=max(arr[i-1],arr[i]+1)
            else:
                continue
        for i in range(n-1):
            if ratings[i+1]>ratings[i]:
                arr[i+1]=max(arr[i]+1,arr[i+1])
            elif ratings[i]>ratings[i+1]:
                arr[i]=max(arr[i],arr[i+1]+1)
            else:
                continue
        return sum(arr)
        