#https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = sum_list = ListNode(None)
        carry = 0
        
        while l1 or l2:
            if l1 and l2:
                if carry == 1:
                    digit_sum = l1.val+l2.val+carry
                    carry = 0
                else:
                    digit_sum = l1.val+l2.val
                
                if digit_sum>=10:
                    digit_sum = digit_sum%10
                    carry = 1
                sum_list.next = (ListNode(digit_sum))
                sum_list = sum_list.next
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2:
                if carry == 1:
                    digit_sum = l2.val+carry
                    carry = 0
                else:
                    digit_sum = l2.val
                
                if digit_sum>=10:
                    digit_sum = digit_sum%10
                    carry = 1
                sum_list.next = (ListNode(digit_sum))
                sum_list = sum_list.next
                l2 = l2.next
            elif l1 and l2 is None:
                if carry == 1:
                    digit_sum = l1.val+carry
                    carry = 0
                else:
                    digit_sum = l1.val
                
                if digit_sum>=10:
                    digit_sum = digit_sum%10
                    carry = 1
                sum_list.next = (ListNode(digit_sum))
                sum_list = sum_list.next
                l1 = l1.next

        if carry == 1:
            sum_list.next = (ListNode(carry))
            sum_list = sum_list.next
            
        return head.next
