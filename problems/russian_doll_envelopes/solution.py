class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def lowerBound(temp,num):
            l=0
            h=len(temp)-1
            while l<=h:
                m=l+(h-l)//2
                if temp[m][1]<num:
                    l=m+1
                else:
                    h=m-1
            return l
        arr=envelopes
        arr.sort(key=lambda x:(x[0],-x[1]))
        temp=[]
        temp.append(arr[0])
        for i in range(1,len(arr)):
            if arr[i][1]>temp[-1][1]:
                temp.append(arr[i])
            else:
                ind=lowerBound(temp,arr[i][1])
                temp[ind]=arr[i]        
        return len(temp)





        