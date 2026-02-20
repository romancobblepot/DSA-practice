# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        #your code goes here
        def dfs(root):
            if not root:
                return 0,float('-inf')
            left_sum,maxi_left=dfs(root.left)
            right_sum,maxi_right=dfs(root.right)
            left_sum=max(0,left_sum)
            right_sum=max(0,right_sum)
            maxi=max(left_sum+root.val+right_sum,maxi_left,maxi_right)
            return max(left_sum,right_sum) + root.val,maxi
        return dfs(root)[1]