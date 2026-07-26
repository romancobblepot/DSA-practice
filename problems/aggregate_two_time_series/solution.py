class Solution(object):
    def aggregateTimeSeries(self, series1, series2):
        """
        :type series1: List[List[int]]
        :type series2: List[List[int]]
        :rtype: List[List[int]]
        """
        n1=len(series1)
        n2=len(series2)
        i=0
        j=0
        arr=[]
        while i<n1 and j<n2:
            timestamp1=series1[i][0]
            timestamp2=series2[j][0]
            if timestamp1<timestamp2:
                arr.append([timestamp1,series1[i][1]+series2[j][1]])
                i+=1
            elif timestamp2<timestamp1:
                arr.append([timestamp2,series2[j][1]+series1[i][1]])
                j+=1
            else:
                arr.append([timestamp1,series2[j][1]+series1[i][1]])
                i+=1
                j+=1
        while i<n1:
            arr.append([series1[i][0],series1[i][1]])
            i+=1
        while j<n2:
            arr.append([series2[j][0],series2[j][1]])
            j+=1
        return arr
                
            
        
            
        
        