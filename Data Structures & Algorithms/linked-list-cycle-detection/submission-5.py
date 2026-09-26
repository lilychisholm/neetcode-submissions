# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #recursion?
        #Wait no we legit just go through the entre linkedlist and chck if the last node's index is -1 lmao
        node = head
        visited = set()
        while True:
            if not node or not node.next:
                return False
            if node.val in visited:
                return True
            visited.add(node.val)
            if node.next:
                node = node.next
