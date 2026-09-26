# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        counter = head
        while counter:
            length += 1
            counter = counter.next
        
        first = curr = head
        count = 0
        while count < length//2 - 1:
            curr = curr.next
            count += 1
        
        second_curr = curr.next
        curr.next = None

        stack = []
        while count < length - 1:
            stack.append(second_curr)
            second_curr = second_curr.next
            count += 1

        second = curr2 = ListNode()
        while stack:
            curr2.next = stack.pop()
            curr2 = curr2.next

        curr2.next = None
        second = second.next

        node = final = ListNode()
        f = True
        while first or second:
            if f and first:
                node.next = first
                first = first.next
                f = False
                node = node.next
            elif second:
                node.next = second
                second = second.next
                f = True
                node = node.next
        final = final.next




        
