class Solution(object):
    def maxRatings(self, units):
        """
        :type units: List[List[int]]
        :rtype: int
        """
        m=len(units)
        units_new=[]
        for i in range(len(units)):
            units[i].sort()
            minimum=units[i][0]
            if len(units[i])>1:
                second_minimum=units[i][1]
            else:
                second_minimum=units[i][0]
            units_new.append([minimum,second_minimum])
        second_min=float('inf')
        for i in range(len(units_new)):
            if units_new[i][1]<=second_min:
                second_min=units_new[i][1]
                ind=i
        sum=0
        for i in range(len(units_new)):
            if i!=ind:
                units_new[ind].append(units_new[i][0])
                sum+=units_new[i][1]
        units_new[ind].sort()
        sum+=units_new[ind][0]
        return sum
            
        
        