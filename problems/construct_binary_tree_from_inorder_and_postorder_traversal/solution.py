# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_map={}
        for i,value in enumerate(inorder):
            inorder_map[value]=i
        def constructTree(in_start,in_end,pos_start,pos_end):
            if in_start>in_end or pos_start>pos_end:
                return 
            root=TreeNode(postorder[pos_end])
            inorder_index=inorder_map[root.val]
            left_subtree_size=inorder_index-in_start
            root.left=constructTree(in_start,inorder_index-1,pos_start,pos_start+left_subtree_size-1)
            root.right=constructTree(inorder_index+1,in_end,pos_start+left_subtree_size,pos_end-1)
            return root
        return constructTree(0,len(inorder)-1,0,len(postorder)-1)
            

        