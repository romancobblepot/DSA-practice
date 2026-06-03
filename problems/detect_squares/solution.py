class DetectSquares(object):

    def __init__(self):
        self.rows=defaultdict(list)
    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        u,v=point
        self.rows[(u,v)]=self.rows.get((u,v),0)+1
    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        u,v=point
        count=0
        for key in self.rows:
            i,j=key
            if j==v:
                    distance=abs(i-u)
                    if distance>0:
                        if (i,v-distance) in self.rows and (u,v-distance) in self.rows:
                            count+=self.rows[(i,v-distance)]*self.rows[(u,v-distance)]*self.rows[(i,v)]
                        if (i,v+distance) in self.rows and (u,v+distance) in self.rows:
                            count+=self.rows[(i,v+distance)]*self.rows[(u,v+distance)]*self.rows[(i,v)]
        return count
        



        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)