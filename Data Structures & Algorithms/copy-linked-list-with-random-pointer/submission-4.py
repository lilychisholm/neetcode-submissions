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
        if not head:
            return None
        oldToNewNodes = dict()
        dummy = head
        while dummy:
            newNode = Node(dummy.val)
            newNode.next = dummy.next
            newNode.random = dummy.random
            oldToNewNodes[dummy] = newNode
            dummy = dummy.next
        
        copy = oldToNewNodes[head]
        while copy:
            if copy.next:
                copy.next = oldToNewNodes[copy.next]
            if copy.random:
                copy.random = oldToNewNodes[copy.random]
            copy = copy.next

        return oldToNewNodes[head]