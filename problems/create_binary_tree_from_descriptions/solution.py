# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        parent_map=defaultdict(list)
        children=set()
        parents=set()
        for parent,child,is_left in descriptions:
            if is_left==1:
                parent_map[parent].append((child,1))
                parents.add(parent)
                children.add(child)
        for parent,child,is_left in descriptions:
            if is_left==0:
                parent_map[parent].append((child,0))
                parents.add(parent)
                children.add(child)
        root=TreeNode(list(parents-children)[0])
        head=root
        q=deque([root])
        while q:
            node=q.popleft()
            for children,is_left in parent_map[node.val]:
                child_node=TreeNode(children)
                if is_left==1:
                    node.left=child_node
                else:
                    node.right=child_node
                q.append(child_node)
        return head
            




        
        

        