class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank_sum=0
        start_index=0
        n=len(gas)
        if sum(gas)<sum(cost):
            return -1
        for i in range(n):
            tank_sum+=gas[i]-cost[i]
            if tank_sum<0:
                tank_sum=0
                start_index=i+1
        return start_index
        