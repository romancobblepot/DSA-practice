# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result=[]
        q=deque([root])
        while q:
            node=q.popleft()
            if not node:
                result.append("#")
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=deque(data.split(","))
        root=TreeNode((data.popleft()))
        q=deque([root])
        if not data:
            return []
        while q:
            node=q.popleft()
            left_val=data.popleft()
            if left_val!="#":
                left_node=TreeNode(int(left_val))
                node.left=left_node
                q.append(left_node)
            right_val=data.popleft()
            if right_val!="#":
                right_node=TreeNode(int(right_val))
                node.right=right_node
                q.append(right_node)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))