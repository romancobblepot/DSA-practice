# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[]
        arr=[]
        def allPaths(root,res,arr):
            if not root:
                return
            res.append(root.val)
            if not root.left and not root.right:
                arr.append(res[:])
            allPaths(root.left,res,arr)
            allPaths(root.right,res,arr)
            res.pop()
        allPaths(root,res,arr)
        sum=0
        for num in arr:
            string=''.join(map(str,num))
            integer=int(string)
            sum+=integer
        return sum
        