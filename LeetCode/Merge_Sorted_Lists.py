#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = meged_list=ListNode(None)
        
        while l1 or l2:
            if l1 and l2:
                if l1.val<l2.val:
                    meged_list.next = ListNode(l1.val)
                    meged_list = meged_list.next
                    l1 = l1.next
                else:
                    meged_list.next = ListNode(l2.val)
                    meged_list = meged_list.next
                    l2 = l2.next
                    
            elif l1 is not None and l2 is None:
                meged_list.next = ListNode(l1.val)
                meged_list = meged_list.next
                l1 = l1.next
                
            elif l2 is not None and l1 is None:
                meged_list.next = ListNode(l2.val)
                meged_list = meged_list.next
                l2 = l2.next
                
        return head.next
