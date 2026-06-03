# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.i=0
        inorder_index_map={value:i for i,value in enumerate(inorder)}
        def helper(left,right):
            if self.i==len(preorder):
                return
            if left>right:
                return
            val=preorder[self.i]
            self.i+=1
            val_index=inorder_index_map[val]
            node=TreeNode(val)
            node.left=helper(left,val_index-1)
            node.right=helper(val_index+1,right)
            return node
        return helper(0,len(preorder)-1)
        


        