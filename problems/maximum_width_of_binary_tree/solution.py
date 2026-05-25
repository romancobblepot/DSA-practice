# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        dq=deque()
        dq.append((root,0))
        max_width=0
        while dq:
            max_index=0
            min_index=float('inf')
            for _ in range(len(dq)):
                node,index=dq.popleft()
                max_index=max(index,max_index)
                min_index=min(index,min_index)
                if node.left:
                    dq.append((node.left,2*index + 1))
                if node.right:
                    dq.append((node.right,2*index + 2))
            max_width=max(max_index-min_index+1,max_width)
        return max_width
            
        