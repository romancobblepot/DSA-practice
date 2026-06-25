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
        if not root:
            return None
        temp=root
        q=deque()
        q.append(root)
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
            for i in range(len(level)-1):
                level[i].next=level[i+1]
        return temp
                

        