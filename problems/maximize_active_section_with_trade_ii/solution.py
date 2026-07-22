class SegementTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.tree=[0]*(4*self.n)
        self.build(arr,0,0,self.n -1)
        self.ones=[]
    def build(self,arr,idx,l,r):
        if l==r:
            self.tree[idx]=arr[l]
            return 
        mid=l+(r-l)//2
        self.build(arr,2*idx+1,l,mid)
        self.build(arr,2*idx+2,mid+1,r)
        self.tree[idx]=self.merge(self.tree[2*idx+1],self.tree[2*idx+2])
    def merge(self,left,right):
        return max(left,right)
    def query(self,idx,l,r,ql,qr):
        if qr<l or ql>r or l>r:
            return 0
        if ql<=l and r<=qr:
            return self.tree[idx]
        mid=l+(r-l)//2
        left_tree=self.query(2*idx+1,l,mid,ql,qr)
        right_tree=self.query(2*idx+2,mid+1,r,ql,qr)
        return self.merge(left_tree,right_tree)
class Solution(object):
    def lowerBound(self,arr,l):
        low=0
        high=len(arr)
        while low<high:
            mid=(low+high)//2
            if arr[mid]>=l:
                high=mid
            else:
                low=mid+1
        return low
    def UpperBound(self,arr,r):
        low=0
        high=len(arr)
        while low<high:
            mid=(low+high)//2
            if arr[mid]>r:
                high=mid
            else:
                low=mid+1
        return low
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total_ones=0
        n=len(s)
        for i in range(n):
            if s[i]=="1":
                total_ones+=1
        n=len(s)
        zeros_len=[]
        zeros_start=[]
        zeros_end=[]
        i=0
        while i<n:
            j=i
            while j<n and (s[j]==s[i]):
                j+=1
            if s[i]=='0':
                zeros_len.append(j-i)
                zeros_start.append(i)
                zeros_end.append(j-1)
            i=j
        if len(zeros_len)<2:
            return [total_ones]*(len(queries))
        gain=[0]*(len(zeros_len)-1)
        for i in range(len(zeros_len)-1):
            gain[i]=zeros_len[i]+zeros_len[i+1]
        st=SegementTree(gain)
        m=len(zeros_len)
        ans=[]
        for q in queries:
            l=q[0]
            r=q[1]
            first_zero_block_partial=self.lowerBound(zeros_end,l)
            last_zero_block_partial=self.UpperBound(zeros_start,r)-1
            if first_zero_block_partial>=last_zero_block_partial or first_zero_block_partial>=m or last_zero_block_partial<0:
                ans.append(total_ones)
                continue
            first_partial_len=zeros_end[first_zero_block_partial]-max(zeros_start[first_zero_block_partial],l)+1
            last_partial_len=min(zeros_end[last_zero_block_partial],r)-zeros_start[last_zero_block_partial]+1
            if first_zero_block_partial+1==last_zero_block_partial:
                ans.append(total_ones+first_partial_len+last_partial_len)
                continue
            maxi=0
            maxi=max(maxi,first_partial_len+zeros_len[first_zero_block_partial+1],last_partial_len+zeros_len[last_zero_block_partial-1])
            int_maxi=st.query(0,0,len(gain)-1,first_zero_block_partial+1,last_zero_block_partial-2)
            maxi=max(maxi,int_maxi)
            ans.append(total_ones+maxi)
        return ans


        

        