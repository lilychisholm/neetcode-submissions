# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #two pointers: one for list1, one for list2
        #since both linkedlists are sorted, we can always be sure that the next item to an item in the linkedlist will be greater than or equal to the current item
        #so, we can rely on the fact that both linkedlists are already sorted in order to create the final soreted linkedlist
        #we can look at both pointers, and see which one is the minimum
        #the minimum will be added to the final linkedlist and have its pointer moved to the next item in the current linkedlist
        #the maximum will stay in place
        #because we can compare both linkedlists in order, we can work through it node by node
        pointer1 = list1
        pointer2 = list2
        final = ListNode()
        
        final_head = final

        while pointer1 or pointer2:
            if pointer1 and pointer2:
                if pointer2.val <= pointer1.val:
                    final.next = pointer2
                    pointer2 = pointer2.next
                else:
                    final.next = pointer1
                    pointer1 = pointer1.next

            elif pointer1:
                final.next = pointer1
                pointer1 = pointer1.next
            else:
                final.next = pointer2
                pointer2 = pointer2.next

            final = final.next

        return final_head.next


        