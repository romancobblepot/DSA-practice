# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def connector(self,root):
        node=root
        if not node.right:
            return node.left
        if not node.left:
            return node.right
        if node.right and node.left:
            left_subtree=node.left
            right_subtree=node.right
            while right_subtree and right_subtree.left:
                right_subtree=right_subtree.left
            right_subtree.left=left_subtree
            return node.right
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        node=root
        if not node: return None
        if root.val==key:
            return self.connector(root)
        while root:
            if root.val<key:
                if root.right and root.right.val==key:
                    root.right=self.connector(root.right)
                    break
                else:
                    root=root.right
            else:
                if root.left and root.left.val==key:
                    root.left=self.connector(root.left)
                    break
                else:
                    root=root.left
        return node
        