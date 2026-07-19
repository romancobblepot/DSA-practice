# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countDominantNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def postOrder(root,maxi):
            if not root:
                return 0,float('-inf')
            left_count,max_left_val=postOrder(root.left,maxi)
            right_count,max_right_val=postOrder(root.right,maxi)
            if max(max_left_val,max_right_val)<=root.val:
                left_count+=1
            new_max=max(root.val,maxi,max_left_val,max_right_val)
            return left_count+right_count,new_max
        return postOrder(root,float('-inf'))[0]
            
            
            
            
            
            
        