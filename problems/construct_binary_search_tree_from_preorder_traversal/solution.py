# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.i=0
        def helper(min_value,max_value):
            if self.i==len(preorder):
                return
            val=preorder[self.i]
            if val>=max_value or val<=min_value:    
                return
            self.i+=1
            node=TreeNode(val)
            node.left=helper(min_value,val)
            node.right=helper(val,max_value)
            return node
        return helper(float('-inf'),float('inf')) 