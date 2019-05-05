#https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numlist = {}
        
        for num in nums:
            if num not in numlist:
                numlist[num]=1
            else:
                numlist[num]+=1
        for num_one in numlist:
            if numlist[num_one] == 1:
                return num_one
