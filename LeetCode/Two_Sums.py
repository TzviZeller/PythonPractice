# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num1 in range(0,len(nums)):
            for num2 in range(1, len(nums)):
                if nums[num1]+nums[num2] == target and num1 != num2:
                    return num1,num2
