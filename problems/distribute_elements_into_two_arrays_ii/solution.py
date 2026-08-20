import bisect
class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res1=[nums[0]]
        arr1=[nums[0]]
        res2=[nums[1]]
        arr2=[nums[1]]
        for i in range(2,len(nums)):
            if (len(arr1)-bisect.bisect_right(arr1,nums[i]))>(len(arr2)-bisect.bisect_right(arr2,nums[i])):
                res1.append(nums[i])
                bisect.insort(arr1,nums[i]) 
            elif (len(arr1)-bisect.bisect_right(arr1,nums[i]))<(len(arr2)-bisect.bisect_right(arr2,nums[i])):
                res2.append(nums[i])
                bisect.insort(arr2,nums[i])
            else:
                if len(arr1)<=len(arr2):
                    res1.append(nums[i])
                    bisect.insort(arr1,nums[i])
                else:
                    res2.append(nums[i])
                    bisect.insort(arr2,nums[i])
        return res1+res2



        