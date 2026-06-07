"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def levelOrder(root):
            if not root:
                return None
            q=deque([root])
            ans=[]
            while q:
                k=len(q)
                level=[]
                for _ in range(k):
                    node=q.popleft()
                    level.append(node)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(level)
            for levels in ans:
                for i in range(len(levels)-1):
                    levels[i].next=levels[i+1]
            return root
        return levelOrder(root)

        
        