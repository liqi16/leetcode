"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        nodedict = dict() #***
        cur = head
        while cur is not None:
            newnode = Node(cur.val)
            nodedict[cur] = newnode
            cur = cur.next

        cur = head
        new_head = nodedict[cur]
        new_cur = new_head
        while cur is not None:
            if cur.next is None:
                new_cur.next = None
            else:
                new_cur.next = nodedict[cur.next]
            if cur.random is None:
                new_cur.random = None
            else:
                new_cur.random = nodedict[cur.random]
            cur = cur.next
            new_cur = new_cur.next
        return new_head
