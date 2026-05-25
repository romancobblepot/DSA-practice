# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def columnorder(self,root,dictionary,row,col):
        if not root:
            return
        dictionary[col].append((row,root.val))
        self.columnorder(root.left,dictionary,row+1,col-1)
        self.columnorder(root.right,dictionary,row+1,col+1)    
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        dictionary=defaultdict(list)
        self.columnorder(root,dictionary,0,0)
        res=[]
        for col in sorted(dictionary):
            dictionary[col].sort()
            res.append([val for row,val in dictionary[col]])
        return res
        

        