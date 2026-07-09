# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        def isleaf(node):
            if not node.left and not node.right:
                return True
            return False
        def dfs(node):
            if not node:
                return 
            if node.left:
                dfs(node.left)
                if node.left.val==target and isleaf(node.left):
                    node.left=None
            if node.right:
                dfs(node.right)
                if node.right.val==target  and isleaf(node.right):
                    node.right=None
            return node
        if isleaf(dfs(root)) and root.val==target:
            return None
        return dfs(root)
        