"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        new_node=Node(node.val)
        q=deque()
        q.append([new_node,node])
        clone={}
        while q:
            neww_node,node=q.popleft()
            neighbour_s=node.neighbors
            arr=[]
            clone[node]=neww_node
            for it in neighbour_s:
                if it not in clone:
                    new_it=Node(it.val)
                    arr.append(new_it)
                    q.append([new_it,it])
                    clone[it]=new_it
                else:
                    arr.append(clone[it])
            neww_node.neighbors=arr
        return new_node





        