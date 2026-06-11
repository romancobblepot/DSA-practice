class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        min_arr=min(arr)
        max_arr=max(arr)
        n=len(arr)
        if x>=max(arr):
            return arr[n-k:]
        elif x<=min(arr):
            return arr[:k]
        else:
            closest_left=-1
            for i in range(len(arr)):
                if arr[i]<=x:
                    closest_left=i
                else:
                    break
            closest_right=n
            for i in range(len(arr)-1,-1,-1):
                if arr[i]>x:
                    closest_right=i
                else:
                    break
            left=closest_left
            right=closest_right
            count=0
            left_elements=[]
            right_elements=[]
            while left>=0 and count<k:
                left_elements.append(arr[left])
                left-=1
                count+=1
            if count<k:
                while count<k:
                    right_elements.append(arr[right])
                    right+=1
                    count+=1
            while left_elements and right<n and abs(x-left_elements[-1])>abs(arr[right]-x):
                left_elements.pop()
                right_elements.append(arr[right])
                right+=1
            if left_elements:
                left_elements.reverse()
            ans=left_elements+right_elements
            return ans
            



        
        