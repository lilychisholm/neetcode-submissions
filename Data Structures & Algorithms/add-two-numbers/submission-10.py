# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # bullshit approach lmao
        # num1 = ""
        # while l1:
        #     num1 = str(l1.val) + num1
        #     l1 = l1.next
        # num2 = ""
        # while l2:
        #     num2 = str(l2.val) + num2
        #     l2 = l2.next
        
        # num = int(num1) + int(num2)

        # num = str(num)[-1::-1]

        # head = curr = ListNode()
        # for letter in num:
        #     curr.next = ListNode()
        #     curr = curr.next
        #     curr.val = int(letter)

        # return head.next

        # actual approach:

        head = curr = ListNode()
        carry = 0
        while l1 or l2:
            num1 = 0
            num2 = 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next

            num = (num1 + num2 + carry) % 10

            curr.next = ListNode()
            curr = curr.next
            curr.val = num

            carry = (num1 + num2 + carry) // 10

        if carry > 0:
            curr.next = ListNode()
            curr = curr.next
            curr.val = carry

        return head.next


        
        