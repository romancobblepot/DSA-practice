class SegementTree():
    def __init__(self,arr):
        self.n=len(arr)
        self.tree=[(float('-inf'),float('inf'))]*(4*self.n)
        self.build(0,0,self.n-1,arr)
    def build(self,idx,l,r,arr):
        if l==r:
            self.tree[idx]=(arr[l],arr[l])
            return 
        mid=l+(r-l)//2
        self.build(2*idx+1,l,mid,arr)
        self.build(2*idx+2,mid+1,r,arr)
        self.tree[idx]=self.merge(self.tree[2*idx+1],self.tree[2*idx+2])
    def merge(self,left,right):
        return (max(left[0],right[0]),min(left[1],right[1]))
    def query(self,idx,l,r,ql,qr):
        if r<ql or qr<l:
            return (float('-inf'),float('inf'))
        if ql<=l and r<=qr:
            return self.tree[idx]
        mid=l+(r-l)//2
        left_build=self.query(2*idx+1,l,mid,ql,qr)
        right_build=self.query(2*idx+2,mid+1,r,ql,qr)
        return self.merge(left_build,right_build)
class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        st=SegementTree(nums)
        l=0
        n=len(nums)
        count=0
        q=[]
        total=0
        for l in range(len(nums)):
            max_,min_=st.query(0,0,n-1,l,n-1)
            heapq.heappush(q,(-(max_-min_),l,n-1))
        for i in range(k):
            diff,l,r=heapq.heappop(q)
            total+=-diff
            if r>l:
                max_,min_=st.query(0,0,n-1,l,r-1)
                heapq.heappush(q,(-(max_-min_),l,r-1))
        return total
        


        

        
        