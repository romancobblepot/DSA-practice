# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node,max_value,min_value):
            if not node:
                return True
            if node.val<=min_value or node.val>=max_value:
                return False
            left_is_valid=check(node.left,node.val,min_value)
            right_is_valid=check(node.right,max_value,node.val)
            if not left_is_valid or not right_is_valid:
                return False
            return True 
        return check(root,float('inf'),float('-inf'))
        