#https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_list=[]
        even_list=[]
        
        for num in A:
            if num%2==0:
                even_list.append(num)
            else:
                odd_list.append(num)
        even_list += odd_list
        return even_list
