# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        dq=deque([root])
        res=[]
        ans=[]
        if not root:
            return []
        while dq:
            level=[]
            for _ in range(len(dq)):
                node=dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level)        
        for level in res:
            ans.append(level[-1])
        return ans
        