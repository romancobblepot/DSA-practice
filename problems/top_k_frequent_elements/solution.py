import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        num_count={}
        arr=[]
        num_count=Counter(nums)
        count=0
        for key in num_count:
            if count<k:
                heapq.heappush(arr,(num_count[key],key))
                count+=1
            else:
                freq,element_0=arr[0]
                if freq<num_count[key]:
                    heapq.heappop(arr)
                    heapq.heappush(arr,(num_count[key],key))
        ans=[]
        for tuple in arr:
            ans.append(tuple[1])
        return ans
        
            
            


        