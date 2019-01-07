#https://leetcode.com/problems/longest-palindrome/

"""Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here."""

class Solution:
    def longestPalindrome(self,s):
      longest = 0
      letters = {}
      for letter in s:
        if not letter.isalpha():
          continue
        if letter in letters:
          letters[letter] += 1
        else:
          letters[letter] = 1
      total = 0
      for count in letters.values():
        total += count // 2 * 2
        if total % 2 == 0 and count % 2 == 1:
          total += 1
      return total
