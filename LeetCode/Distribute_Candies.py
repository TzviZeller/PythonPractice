#https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        candiesList = []
        for i in range(len(candies)):
            if candies[i] not in candiesList:
                candiesList.append(i)
        
        if len(candies)/2 < len(candiesList):
            return int(len(candies)/2)
        else:
            return len(candiesList)

