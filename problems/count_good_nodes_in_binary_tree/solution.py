# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0
        def dfs(prev_value,root):
            if not root:
                return
            if root.val>=prev_value:
                self.count+=1
                prev_value=root.val
            dfs(prev_value,root.left)
            dfs(prev_value,root.right)
        dfs(float('-inf'),root)
        return self.count

            
        