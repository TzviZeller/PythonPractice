#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        bob = valid = ListNode(None)
        dict_dedupe = {}
        
        while head:
            if head.val in dict_dedupe:
                dict_dedupe[head.val]+=1
                head = head.next
            else:
                dict_dedupe[head.val]=1
                head = head.next
        
        for key,val in dict_dedupe.items():
            if val==1:
                valid.next= ListNode(key)
                valid = valid.next
        return bob.next
        
