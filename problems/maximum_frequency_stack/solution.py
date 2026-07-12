class FreqStack(object):

    def __init__(self):
        self.element_mapp=defaultdict(int)
        self.pq=[]
        self.count=0
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.element_mapp[val]+=1
        self.count+=1
        heapq.heappush(self.pq,(-self.element_mapp[val],-self.count,val))
    def pop(self):
        """
        :rtype: int
        """
        max_freq,c,element=heapq.heappop(self.pq)
        self.element_mapp[element]-=1
        return element
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()