# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        stack=[]
        self.next_element=TreeNode()
        self.stack=stack
        node=root
        while node:
            stack.append(node)
            node=node.left

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            self.next_element=self.stack.pop()
        if self.next_element.right:
            current=self.next_element.right
            while current:
                self.stack.append(current)
                current=current.left
        return self.next_element.val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()