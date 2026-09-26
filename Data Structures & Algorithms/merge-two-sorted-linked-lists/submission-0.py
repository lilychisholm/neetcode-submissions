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
        dummy = node = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list2.val <= list1.val:
                    node.next = list2
                    list2 = list2.next
                else:
                    node.next = list1
                    list1 = list1.next
            elif list1:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        return dummy.next




        