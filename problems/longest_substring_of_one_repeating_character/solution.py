class SegementTree(object):
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=list(arr)
        self.tree=[None]*(4*self.n)
        self.build(arr,0,0,self.n -1)
    def build(self,arr,idx,l,r):
        if l==r:
            char=self.arr[l]
            self.tree[idx]=(1,char,1,char,1)
            return
        mid=l+(r-l)//2
        self.build(arr,2*idx+1,l,mid)
        self.build(arr,2*idx+2,mid+1,r)
        self.tree[idx]=self.merge(self.tree[2*idx+1],self.tree[2*idx+2],mid-l+1,r-mid)
    def merge(self,left_child,right_child,left_size,right_size):
        l_max_len,l_prefix_char,l_prefix_len,l_suffix_char,l_suffix_len=left_child
        r_max_len,r_prefix_char,r_prefix_len,r_suffix_char,r_suffix_len=right_child
        parent_max_len=max(l_max_len,r_max_len)
        parent_prefix_char=l_prefix_char
        if l_prefix_len==left_size and l_prefix_char==r_prefix_char:
            parent_prefix_len=left_size+r_prefix_len
        else:
            parent_prefix_len=l_prefix_len
        parent_suffix_char=r_suffix_char
        if r_suffix_len==right_size and l_suffix_char==r_suffix_char:
            parent_suffix_len=right_size+l_suffix_len
        else:
            parent_suffix_len=r_suffix_len
        if l_suffix_char==r_prefix_char:
            parent_max_len=max(parent_max_len,l_suffix_len+r_prefix_len)
        return (parent_max_len,parent_prefix_char,parent_prefix_len,parent_suffix_char,parent_suffix_len)
    def update(self,idx,l,r,pos,new_char):
        if l==r:
            self.arr[pos]=new_char
            self.tree[idx]=(1,new_char,1,new_char,1)
            return
        mid=l+(r-l)//2
        if pos<=mid:
            self.update(2*idx+1,l,mid,pos,new_char)
        else:
            self.update(2*idx +2,mid+1,r,pos,new_char)
        self.tree[idx]=self.merge(self.tree[2*idx+1],self.tree[2*idx +2],mid-l+1,r-mid)
class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n=len(s)
        ans=[]
        st=SegementTree(s)
        for i,pos in enumerate(queryIndices):
            new_char=queryCharacters[i]
            st.update(0,0,n-1,pos,new_char)
            max_len=st.tree[0][0]
            ans.append(max_len)
        return ans




        