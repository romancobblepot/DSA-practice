# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        queue=deque([root])
        lefttoRight=True
        while queue:
            size=len(queue)
            level=[0]*size
            for i in range(size):
                node=queue.popleft()
                rowindex=i if lefttoRight else (size-1-i)
                level[rowindex]=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lefttoRight= not lefttoRight
            res.append(level)
        return res
        