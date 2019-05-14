#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        not_repeted = {}
        count = 0
        for num in nums:
            if num not in not_repeted.keys():
                not_repeted[num] = 1
            else:
                not_repeted[num] +=1
        #bad question wont let me return this as an answer
        print(not_repeted.keys()) 
