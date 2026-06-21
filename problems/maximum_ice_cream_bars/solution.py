class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_arr=max(costs)
        cnt_arr=[0]*(max_arr+1)
        ans=[0]*len(costs)
        for num in costs:
            cnt_arr[num]+=1
        for i in range(1,max_arr+1):
            cnt_arr[i]+=cnt_arr[i-1]
        for i in range(len(costs)-1,-1,-1):
            v=costs[i]
            ans[cnt_arr[v]-1]=v
            cnt_arr[v]-=1
        prefix_sum=[0]*(len(costs)+1)
        output=0
        for i in range(1,len(costs)+1):
            prefix_sum[i]+=prefix_sum[i-1]+ans[i-1]
            if prefix_sum[i]<=coins:
                output=i
            else:
                break
        return output


        
        
        