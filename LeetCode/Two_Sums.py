# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num2=1
        for num1 in range(len(nums)):
            for num2 in range(len(nums)):
                if num1!=num2 and nums[num1]+nums[num2]==target:
                        return [num1, num2]
