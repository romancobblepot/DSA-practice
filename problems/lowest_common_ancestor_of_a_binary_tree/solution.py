# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self,root,p,q):
        if not root:
            return
        if root==p or root==q:
            return root
        left_found=self.isSame(root.left,p,q)
        right_found=self.isSame(root.right,p,q)
        if left_found and right_found:
            return root
        if left_found:
            return left_found
        if right_found:
            return right_found  
    def lowestCommonAncestor(self, root, p, q):
        return self.isSame(root,p,q)
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        