class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        row=0
        col=m-1
        # Perform binary search
        while 0<=row<n and 0<=col<m:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            elif matrix[row][col]>target:
                col-=1
        # Return false if target is not found
        return False   
        