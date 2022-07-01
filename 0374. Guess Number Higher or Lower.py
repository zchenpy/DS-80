374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/
  
  
# Binary Search
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r  = 0, n+1
        while l + 1 != r:
            m = l + (r - l)//2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m
            else:
                r = m  
#Time complexity: O(logn)
#Space complexity:O(1)                
