# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #numbers stored in reverse of order
        #take each linked list, put into stack
        #as you pop, multiply value by 10 ^ len(stack) - 1 then add to number total
        #add final numbers

        num1 = 0
        stack = []
        while l1:
            stack.append(l1.val)
            l1 = l1.next

        while stack:
            num = stack.pop()
            num1 += num * (10**len(stack))
        
        num2 = 0
        while l2:
            stack.append(l2.val)
            l2 = l2.next

        while stack:
            num = stack.pop()
            num2 += num * (10 ** len(stack))

        final = reversed(str(num1 + num2))
        head = curr = ListNode()
        for char in final:
            curr.next = ListNode()
            curr = curr.next
            curr.val = int(char)

        return head.next

        
      