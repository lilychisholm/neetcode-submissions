# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        num2 = ""
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        num = int(num1) + int(num2)

        num = str(num)[-1::-1]

        head = curr = ListNode()
        for letter in num:
            curr.next = ListNode()
            curr = curr.next
            curr.val = int(letter)

        return head.next

        
        