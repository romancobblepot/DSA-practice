"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.dummy=Node(10**5,None,None)
        self.cloned={}
        self.i=0
        self.tempo=self.dummy
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        temp=head
        while temp:
            if temp not in self.cloned:
                new_node=Node(temp.val)
                self.cloned[temp]=new_node
                if not temp.next:
                    new_node.next=None
                elif temp.next not in self.cloned:
                    new_temp_next=Node(temp.next.val)
                    self.cloned[temp.next]=new_temp_next
                    new_node.next=new_temp_next
                else:
                    new_node.next=self.cloned[temp.next]
                if not temp.random:
                    new_node.random=None                
                elif temp.random not in self.cloned:
                    new_random=Node(temp.random.val)
                    self.cloned[temp.random]=new_random
                    new_node.random=new_random
                else:
                    new_node.random=self.cloned[temp.random]
            else:
                new_node=self.cloned[temp]
                if not temp.next:
                    new_node.next=None
                elif temp.next not in self.cloned:
                    new_temp_next=Node(temp.next.val)
                    self.cloned[temp.next]=new_temp_next
                    new_node.next=new_temp_next
                else:
                    new_node.next=self.cloned[temp.next]
                if not temp.random:
                    new_node.random=None
                elif temp.random not in self.cloned:
                    new_random=Node(temp.random.val)
                    self.cloned[temp.random]=new_random
                    new_node.random=new_random
                else:
                    new_node.random=self.cloned[temp.random]
            self.dummy.next=new_node
            self.dummy=new_node
            temp=temp.next
        return self.tempo.next
            



        