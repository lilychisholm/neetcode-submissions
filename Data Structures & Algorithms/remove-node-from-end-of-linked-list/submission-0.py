# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        minus_n, end = ListNode(), head
        final = minus_n
        count = 1
        while count < n:
            end = end.next
            count += 1

        minus_n.next = head
        
        while end.next:
            minus_n = minus_n.next
            end = end.next

        minus_n.next = minus_n.next.next

        return final.next