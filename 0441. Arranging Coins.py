441. Arranging Coins
https://leetcode.com/problems/arranging-coins/
  
#Binary Search
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n+1
        while l+1 != r:
            m = l +(r-l)//2
            if (1+m)*m/2 <= n: 
                l = m 
            else:
                r = m
        return l 
      
#Time complexity: O(logn)
#Space complexity:O(1)



# math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 1        
        coin_count = 1
        while coin_count <= n: 
            row += 1
            coin_count += row
        return row-1  
      
#Time complexity: O(n)
#Space complexity:O(n)
