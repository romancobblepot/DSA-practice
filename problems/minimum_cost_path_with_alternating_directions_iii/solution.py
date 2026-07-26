class Solution(object):
    def minCost(self, m, n, penalty):
        """
        :type m: int
        :type n: int
        :type penalty: List[List[int]]
        :rtype: int
        """
        def isValid(i,j):
            if i<0 or i>=m or j<0 or j>=n: return False
            return True
        odd_moves=[(0,1),(1,0)]
        even_moves=[(0,-1),(-1,0)]
        q=[]
        heapq.heappush(q,(1,0,0,1))
        min_cost=[[[float('inf')]*2 for _ in range(n)] for _ in range(m)]
        while q:
            total_cost,i,j,action=heapq.heappop(q)
            penalty_current=penalty[i][j]
            if action%2==0:
                if total_cost>min_cost[i][j][0]:
                    continue
            else:
                if total_cost>min_cost[i][j][1]:
                    continue
            for k in range(2):
                nrow=i+odd_moves[k][0]
                ncol=j+odd_moves[k][1]
                if isValid(nrow,ncol):
                    entrance_cost=(nrow+1)*(ncol+1)                 
                    if action%2!=0:
                        if total_cost+entrance_cost<min_cost[nrow][ncol][0]:
                            min_cost[nrow][ncol][0]=total_cost+entrance_cost
                            heapq.heappush(q,(min_cost[nrow][ncol][0],nrow,ncol,action+1))
                    else:
                        if total_cost+entrance_cost+penalty_current<min_cost[nrow][ncol][1]:
                            min_cost[nrow][ncol][1]=total_cost+entrance_cost+penalty_current
                            heapq.heappush(q,(min_cost[nrow][ncol][1],nrow,ncol,action+1))
            for k in range(2):
                nrow=i+even_moves[k][0]
                ncol=j+even_moves[k][1]
                if isValid(nrow,ncol):
                    entrance_cost=(nrow+1)*(ncol+1)                 
                    if action%2==0:
                            if total_cost+entrance_cost<min_cost[nrow][ncol][1]:
                                min_cost[nrow][ncol][1]=total_cost+entrance_cost                            
                                heapq.heappush(q,(min_cost[nrow][ncol][1],nrow,ncol,action+1))
                    else:
                            if total_cost+entrance_cost+penalty_current<min_cost[nrow][ncol][0]:
                                min_cost[nrow][ncol][0]=total_cost+entrance_cost+penalty_current
                                heapq.heappush(q,(min_cost[nrow][ncol][0],nrow,ncol,action+1))
            if action%2==0:
                if total_cost+penalty_current<min_cost[i][j][1]:
                    min_cost[i][j][1]=total_cost+penalty_current
                    heapq.heappush(q,(min_cost[i][j][1],i,j,action+1))
            else:
                if total_cost+penalty_current<min_cost[i][j][0]:
                    min_cost[i][j][0]=total_cost+penalty_current
                    heapq.heappush(q,(min_cost[i][j][0],i,j,action+1))
        return min(min_cost[m-1][n-1][0],min_cost[m-1][n-1][1])
        
                    
                        
                    
                    
                    
                
                
                        
                
        
        