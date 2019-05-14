#https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        self.permutations_helper(nums, [], permutations)
        return permutations    
        
    def permutations_helper(self, nums, solution, permutations):
        if len(nums) == 0:
            permutations.append(solution[:])
        else:
            for idx in range(len(nums)):
                solution.append(nums[idx])
                self.permutations_helper(nums[:idx] + nums[idx+1:], solution, permutations)
                solution.pop()        
